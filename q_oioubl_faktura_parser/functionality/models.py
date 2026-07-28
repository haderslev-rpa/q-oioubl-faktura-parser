"""
Datamodeller.

BAGUDKOMPATIBILITET

Eksisterende felter må ALDRIG:
- fjernes
- omdøbes
- ændre datatype

Nye felter må gerne tilføjes.
"""

HEADER_MODEL = {
    "schema_version": "1.2",

    "document_type": "",

    "invoice_id": "",
    "order_reference": "",
    "invoice_date": "",

    "customer_name": "",
    "supplier_name": "",

    "endpoint_id": "",
    "company_id": "",

    "cpr": "",
    "cvr": "",

    "cpr_source": "",
    "cvr_source": "",

    "dimension_account": "",

    "additional_information": "",

    "total_amount": "",
    "vat_amount": "",
    "payable_amount": "",
}


LINE_MODEL = {
    "line_number": "",

    "item_id": "",
    "item_name": "",

    "description": "",
    "note": "",

    "line_amount": "",
    "vat_amount": "",

    "cpr": [],

    "all_details": "",

    "raw_data": {},
}


RESULT_MODEL = {
    "header": {},

    "lines": [],

    "candidates": {
        "cpr_numbers": [],
        "cvr_numbers": [],
        "ean_numbers": [],
    },

    "flattened_xml": {},

    "raw_xml": {},
}