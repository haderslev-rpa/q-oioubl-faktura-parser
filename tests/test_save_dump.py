"""
Gemmer parser output.

Kør:

uv run python tests/test_save_dump.py
"""

from q_oioubl_faktura_parser.functionality.debug import (
    save_debug_dump,
)

from q_oioubl_faktura_parser.functionality.parser import (
    OIOUBLParser,
)


xml_path = (
    r"\\dk-p365-haaos01.prisme-365.dk"
    r"\Aos-storage"
    r"\documents"
    r"\D9C57576-DDF4-4354-BE37-127CBB378550"
)

#7DF121F9-9D98-4819-8CCC-03A797D9A524
#93A6F151-BAB2-45FF-B542-3B1B8B585B7D
#D9D40CB5-F4B6-4BEE-A8EB-C5464FE9202C
#2D0FA267-8262-4DD1-844E-D49A2BE8C651
#D9C57576-DDF4-4354-BE37-127CBB378550
#90EC7B19-CBDC-42F0-A7BF-B77DAEDECD3F
#F65AD0FD-D933-4572-BBCD-911AD9561245


parser = OIOUBLParser()

result = parser.parse(
    xml_path
)

save_debug_dump(
    result
)

print(
    "✅ Dump gemt"
)