"""
Vis rigtigt parser-output.

Bruger ægte data.

Ingen anonymisering.

Kør:

uv run python tests/test_real_output.py
"""

import json

from q_oioubl_faktura_parser.functionality.parser import (
    OIOUBLParser,
)


xml_path = (
    r"\\dk-p365-haaos01.prisme-365.dk"
    r"\Aos-storage"
    r"\documents"
    r"\7DF121F9-9D98-4819-8CCC-03A797D9A524"
)

parser = OIOUBLParser()

result = parser.parse(
    xml_path
)

print()
print("=" * 100)
print("HEADER")
print("=" * 100)

print(
    json.dumps(
        result["header"],
        indent=4,
        ensure_ascii=False,
        default=str,
    )
)

print()
print("=" * 100)
print("LINJER")
print("=" * 100)

for line in result["lines"]:

    print()

    print(
        json.dumps(
            line,
            indent=4,
            ensure_ascii=False,
            default=str,
        )
    )