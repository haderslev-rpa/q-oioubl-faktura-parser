"""
Tester flere XML filer.

For hver XML:

- Parser filen
- Printer resultat
- Gemmer header + lines
  i én samlet dump-fil

Kør:

uv run python tests/test_many_files.py
"""

from q_oioubl_faktura_parser.functionality.parser import (
    OIOUBLParser,
)

from q_oioubl_faktura_parser.functionality.debug import (
    save_debug_dump,
)


XML_FILES = [

    r"\\dk-p365-haaos01.prisme-365.dk\Aos-storage\documents\7DF121F9-9D98-4819-8CCC-03A797D9A524",

    r"\\dk-p365-haaos01.prisme-365.dk\Aos-storage\documents\93A6F151-BAB2-45FF-B542-3B1B8B585B7D",

    r"\\dk-p365-haaos01.prisme-365.dk\Aos-storage\documents\7DF121F9-9D98-4819-8CCC-03A797D9A524",

    r"\\dk-p365-haaos01.prisme-365.dk\Aos-storage\documents\9AE1236E-2CB3-4A0B-81A5-B42CA6019D06",

    r"\\dk-p365-haaos01.prisme-365.dk\Aos-storage\documents\ACF8EA62-0ECB-4F37-938D-CA4E081D35B7",

    r"\\dk-p365-haaos01.prisme-365.dk\Aos-storage\documents\F42BC06E-4126-4688-80AC-046614085693",

    r"\\dk-p365-haaos01.prisme-365.dk\Aos-storage\documents\3753FE82-5DC6-43AE-A78B-C423D2BEAF65",

    r"\\dk-p365-haaos01.prisme-365.dk\Aos-storage\documents\067A3C8A-40A0-4343-8010-D56143181706",

    r"\\dk-p365-haaos01.prisme-365.dk\Aos-storage\documents\427B4678-8E81-4BBE-B127-3CE26E235A5D",

    r"\\dk-p365-haaos01.prisme-365.dk\Aos-storage\documents\20B355B4-1AD1-441B-822F-9D4F0B9DB8CF",

    r"\\dk-p365-haaos01.prisme-365.dk\Aos-storage\documents\F65AD0FD-D933-4572-BBCD-911AD9561245",

    r"\\dk-p365-haaos01.prisme-365.dk\Aos-storage\documents\E62F7074-FD82-4EAA-9538-B7EB7AD19C56",

    r"\\dk-p365-haaos01.prisme-365.dk\Aos-storage\documents\D9C57576-DDF4-4354-BE37-127CBB378550",

    r"\\dk-p365-haaos01.prisme-365.dk\Aos-storage\documents\01C7290D-67F7-45F2-8FAC-E7A22A5E8D32",

    r"\\dk-p365-haaos01.prisme-365.dk\Aos-storage\documents\F94CA532-4FD5-4954-892E-2439B25350C2",

    r"\\dk-p365-haaos01.prisme-365.dk\Aos-storage\documents\DB856913-7A7B-49F0-900A-A868E9D4EAF9",

    r"\\dk-p365-haaos01.prisme-365.dk\Aos-storage\documents\3478ABCB-D46F-4737-B124-3168B2A2EF3E",

    r"\\dk-p365-haaos01.prisme-365.dk\Aos-storage\documents\88A0777B-AA8F-4E9F-BE39-96757974DE22",

    r"\\dk-p365-haaos01.prisme-365.dk\Aos-storage\documents\B5282552-92FF-42C7-A102-C6610AC132B0",

    r"\\dk-p365-haaos01.prisme-365.dk\Aos-storage\documents\4E138541-9A43-48DF-BAF7-EBA374C8695D",

    r"\\dk-p365-haaos01.prisme-365.dk\Aos-storage\documents\2D0FA267-8262-4DD1-844E-D49A2BE8C651",

    r"\\dk-p365-haaos01.prisme-365.dk\Aos-storage\documents\0A12C921-3EA0-41B8-AD42-1F2BEFE2F9EA",

    r"\\dk-p365-haaos01.prisme-365.dk\Aos-storage\documents\D802E79B-47A8-4F57-86EF-E259E106E0D3",

    r"\\dk-p365-haaos01.prisme-365.dk\Aos-storage\documents\298C42EF-156E-457C-A5E4-0A6D14599F88",

    r"\\dk-p365-haaos01.prisme-365.dk\Aos-storage\documents\DB855B77-FA47-4A2F-BC5A-61BE4A49693D",

    r"\\dk-p365-haaos01.prisme-365.dk\Aos-storage\documents\87CF73BE-7B5F-4F59-9EF4-96CFD071C462",

    r"\\dk-p365-haaos01.prisme-365.dk\Aos-storage\documents\9AF31827-826C-4439-BF68-1C23928A8D20",

    r"\\dk-p365-haaos01.prisme-365.dk\Aos-storage\documents\9A833A54-D665-4F7A-A35A-9366DAF0BF83",

    r"\\dk-p365-haaos01.prisme-365.dk\Aos-storage\documents\E5F7BAEE-DAA7-4D4D-BC03-6E9D97479D19",

    r"\\dk-p365-haaos01.prisme-365.dk\Aos-storage\documents\E8814A4F-E410-42AC-8888-8440E82869DA",

    r"\\dk-p365-haaos01.prisme-365.dk\Aos-storage\documents\64FCF96A-09B8-4749-BC57-DC4DA41E502E",

    r"\\dk-p365-haaos01.prisme-365.dk\Aos-storage\documents\90EC7B19-CBDC-42F0-A7BF-B77DAEDECD3F",

    r"\\dk-p365-haaos01.prisme-365.dk\Aos-storage\documents\310F659B-4B2E-4B21-9A57-FF1EBEF0ED53",

    r"\\dk-p365-haaos01.prisme-365.dk\Aos-storage\documents\CC4C89F9-0090-4E6C-BDCC-1FFE6D3CC115",

    r"\\dk-p365-haaos01.prisme-365.dk\Aos-storage\documents\9E6678C6-3274-4918-8ECA-DDA45D675DD8",

    r"\\dk-p365-haaos01.prisme-365.dk\Aos-storage\documents\0B93CB7C-3782-411E-A583-B40ACD96E44E",

    r"\\dk-p365-haaos01.prisme-365.dk\Aos-storage\documents\D9D40CB5-F4B6-4BEE-A8EB-C5464FE9202C",

]

parser = OIOUBLParser()

all_results = []

for file_path in XML_FILES:

    print()
    print("=" * 100)
    print(file_path)
    print("=" * 100)

    try:

        result = parser.parse(
            file_path
        )

        print(
            "Invoice ID:",
            result["header"]["invoice_id"]
        )

        print(
            "Linjer:",
            len(
                result["lines"]
            )
        )

        print(
            "Total:",
            result["header"]["payable_amount"]
        )

        #
        # KUN HEADER + LINES
        #

        all_results.append(
            {
                "file_path": file_path,
                "header": result["header"],
                "lines": result["lines"],
            }
        )

    except Exception as ex:

        print()
        print("FEJL")
        print(type(ex))
        print(ex)

        all_results.append(
            {
                "file_path": file_path,
                "error": str(ex),
            }
        )

#
# ÉN samlet dump-fil
#

save_debug_dump(
    all_results,
    filename="parsed_xml_dump.txt",
)

print()
print("=" * 100)
print("✅ parsed_xml_dump.txt er oprettet")
print("=" * 100)