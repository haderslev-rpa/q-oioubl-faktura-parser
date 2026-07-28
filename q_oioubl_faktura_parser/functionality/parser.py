"""
OIOUBL parser.
"""

import copy

from pathlib import Path

import xmltodict

from .helpers import (
    CVR_REGEX,
    EAN_REGEX,
    build_all_details,
    extract_cpr_numbers,
    extract_text,
    find_all,
    find_first,
    flatten_xml,
    normalize_value,
)

from .models import (
    HEADER_MODEL,
    LINE_MODEL,
    RESULT_MODEL,
)

from .storage import (
    StorageClient,
)

from .xml_mapping import (
    HEADER_MAPPING,
    LINE_MAPPING,
)


class OIOUBLParser:

    def parse(
        self,
        xml_input: str,
    ) -> dict:

        xml_text = self._load_xml(
            xml_input
        )

        xml_data = xmltodict.parse(
            xml_text
        )

        result = copy.deepcopy(
            RESULT_MODEL
        )

        result["header"] = (
            self._build_header(
                xml_data
            )
        )

        result["lines"] = (
            self._build_lines(
                xml_data
            )
        )

        result["raw_xml"] = (
            xml_data
        )

        result["flattened_xml"] = (
            flatten_xml(
                xml_data
            )
        )

        self._scan_candidates(
            result
        )

        return result

    def _load_xml(
        self,
        xml_input: str,
    ) -> str:

        if (
            xml_input
            .lstrip()
            .startswith("<")
        ):
            return xml_input

        if xml_input.startswith(
            "\\\\"
        ):

            storage = StorageClient()

            return storage.read_text(
                xml_input
            )

        return Path(
            xml_input
        ).read_text(
            encoding="utf-8"
        )

    def _build_header(
        self,
        xml_data,
    ):

        header = copy.deepcopy(
            HEADER_MODEL
        )

        for (
            field_name,
            xml_field,
        ) in HEADER_MAPPING.items():

            value = find_first(
                xml_data,
                xml_field,
            )

            header[field_name] = (
                normalize_value(
                    value
                )
            )

        if "Invoice" in xml_data:

            header[
                "document_type"
            ] = "Invoice"

        elif "CreditNote" in xml_data:

            header[
                "document_type"
            ] = "CreditNote"

        supplier_name = find_first(
            xml_data,
            "RegistrationName",
        )

        header[
            "supplier_name"
        ] = normalize_value(
            supplier_name
        )

        customer_name = find_first(
            xml_data,
            "PartyName",
        )

        header[
            "customer_name"
        ] = normalize_value(
            customer_name
        )

        return header

    def _build_lines(
        self,
        xml_data,
    ):

        result = []

        invoice_lines = find_all(
            xml_data,
            "InvoiceLine",
        )

        credit_note_lines = find_all(
            xml_data,
            "CreditNoteLine",
        )

        all_lines = (
            invoice_lines
            + credit_note_lines
        )

        for line in all_lines:

            row = copy.deepcopy(
                LINE_MODEL
            )

            for (
                field_name,
                xml_field,
            ) in LINE_MAPPING.items():

                value = find_first(
                    line,
                    xml_field,
                )

                row[field_name] = (
                    normalize_value(
                        value
                    )
                )

            row["all_details"] = (
                build_all_details(
                    line
                )
            )

            row["cpr"] = (
                extract_cpr_numbers(
                    row["all_details"]
                )
            )

            row["raw_data"] = line

            result.append(
                row
            )

        return result

    def _scan_candidates(
        self,
        result,
    ):

        all_text = extract_text(
            result["raw_xml"]
        )

        text = "\n".join(
            all_text
        )

        cvr_hits = list(
            set(
                CVR_REGEX.findall(
                    text
                )
            )
        )

        ean_hits = list(
            set(
                EAN_REGEX.findall(
                    text
                )
            )
        )

        result["candidates"][
            "cvr_numbers"
        ] = cvr_hits

        result["candidates"][
            "ean_numbers"
        ] = ean_hits

        if cvr_hits:

            result["header"][
                "cvr"
            ] = cvr_hits[0]

        if (
            not result["header"][
                "endpoint_id"
            ]
            and ean_hits
        ):

            result["header"][
                "endpoint_id"
            ] = ean_hits[0]