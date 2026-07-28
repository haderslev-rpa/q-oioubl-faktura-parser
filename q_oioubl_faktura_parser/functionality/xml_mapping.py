"""
Standardfelter.

Eksisterende felter må ikke:
- fjernes
- omdøbes
"""

HEADER_MAPPING = {
    "invoice_id": "ID",

    "invoice_date": "IssueDate",

    "order_reference": "OrderReference",

    "endpoint_id": "EndpointID",

    "company_id": "CompanyID",

    "dimension_account": "AccountingCost",

    "additional_information": "Note",

    "payable_amount": "PayableAmount",
}


LINE_MAPPING = {
    "line_number": "ID",

    "item_id": "SellersItemIdentification",

    "item_name": "Name",

    "description": "Description",

    "note": "Note",

    "line_amount": "LineExtensionAmount",

    "vat_amount": "TaxAmount",
}