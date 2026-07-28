"""
Generelle hjælpefunktioner.
"""

import re
from datetime import datetime


CPR_PATTERN = re.compile(
    r"\b(?:\d{6}-\d{4}|\d{10})\b"
)

CVR_REGEX = re.compile(
    r"\b\d{8}\b"
)

EAN_REGEX = re.compile(
    r"\b\d{13}\b"
)


def clean_tag(tag: str) -> str:

    return tag.split(":")[-1]


def normalize_value(value):

    if value is None:
        return ""

    if isinstance(value, str):
        return value.strip()

    if isinstance(value, dict):

        if "#text" in value:
            return str(
                value["#text"]
            ).strip()

        if "Name" in value:
            return normalize_value(
                value["Name"]
            )

        if "ID" in value:
            return normalize_value(
                value["ID"]
            )

    return value


def normalize_cpr(
    cpr: str,
) -> str:

    return cpr.replace(
        "-",
        "",
    )


def is_valid_cpr(
    cpr: str,
) -> bool:
    """
    Simpel CPR-validering.

    Kontrollerer:
    - længde
    - gyldig dato

    Ikke modulus-kontrol.
    """

    cpr = normalize_cpr(
        cpr
    )

    if len(cpr) != 10:
        return False

    date_part = cpr[:6]

    for year in range(
        1850,
        2100,
    ):

        try:

            datetime.strptime(
                (
                    date_part
                    + str(year)[-2:]
                ),
                "%d%m%Y",
            )

            return True

        except ValueError:
            pass

    return False


def extract_cpr_numbers(
    text: str,
) -> list[str]:
    """
    Finder CPR-numre.

    Returnerer:
        [
         383"
        ]
    """

    result = []

    hits = CPR_PATTERN.findall(
        text
    )

    for hit in hits:

        normalized = (
            normalize_cpr(hit)
        )

        if is_valid_cpr(
            normalized
        ):

            result.append(
                normalized
            )

    return sorted(
        set(result)
    )


def find_first(
    node,
    key,
):

    if isinstance(
        node,
        dict,
    ):

        for (
            child_key,
            value,
        ) in node.items():

            if (
                clean_tag(
                    child_key
                )
                == key
            ):
                return value

            result = find_first(
                value,
                key,
            )

            if result is not None:
                return result

    elif isinstance(
        node,
        list,
    ):

        for item in node:

            result = find_first(
                item,
                key,
            )

            if result is not None:
                return result

    return None


def find_all(
    node,
    key,
):

    result = []

    if isinstance(
        node,
        dict,
    ):

        for (
            child_key,
            value,
        ) in node.items():

            if (
                clean_tag(
                    child_key
                )
                == key
            ):

                if isinstance(
                    value,
                    list,
                ):

                    result.extend(
                        value
                    )

                else:

                    result.append(
                        value
                    )

            result.extend(
                find_all(
                    value,
                    key,
                )
            )

    elif isinstance(
        node,
        list,
    ):

        for item in node:

            result.extend(
                find_all(
                    item,
                    key,
                )
            )

    return result


def extract_text(node):

    values = []

    if isinstance(
        node,
        dict,
    ):

        for value in node.values():

            values.extend(
                extract_text(
                    value
                )
            )

    elif isinstance(
        node,
        list,
    ):

        for item in node:

            values.extend(
                extract_text(
                    item
                )
            )

    elif node is not None:

        values.append(
            str(node)
        )

    return values


def build_all_details(
    node,
) -> str:

    values = extract_text(
        node
    )

    values = [
        str(value).strip()
        for value in values
        if str(value).strip()
    ]

    return " ".join(
        values
    )


def flatten_xml(
    node,
    parent_key="",
):

    result = {}

    if isinstance(
        node,
        dict,
    ):

        for (
            key,
            value,
        ) in node.items():

            clean_key = (
                clean_tag(
                    key
                )
            )

            new_key = (
                f"{parent_key}.{clean_key}"
                if parent_key
                else clean_key
            )

            result.update(
                flatten_xml(
                    value,
                    new_key,
                )
            )

    elif isinstance(
        node,
        list,
    ):

        for (
            index,
            item,
        ) in enumerate(
            node
        ):

            result.update(
                flatten_xml(
                    item,
                    f"{parent_key}[{index}]",
                )
            )

    else:

        result[parent_key] = node

    return result