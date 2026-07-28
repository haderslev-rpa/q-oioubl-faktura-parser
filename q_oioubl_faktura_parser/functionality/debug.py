"""
Debug funktioner.

Formål:

- Gemme parser-output
- Anonymisere data
- Gøre det sikkert at sende dumps

Filen overskrives altid.
"""

import json
import re
from pathlib import Path


def anonymize_text(
    text: str,
) -> str:
    """
    Fjerner alle CPR-lignende værdier.

    Bruges kun til debug dumps.
    """

    #
    # CPR med bindestreg
    #

    text = re.sub(
        r"\b\d{6}-\d{4}\b",
        "XXXXXX-XXXX",
        text,
    )

    #
    # CPR uden bindestreg
    #

    text = re.sub(
        r"\b\d{10}\b",
        "XXXXXXXXXX",
        text,
    )

    return text


def save_debug_dump(
    data,
    filename: str = (
        "parsed_xml_dump.txt"
    ),
):
    """
    Gemmer parser-output.

    Overskriver eksisterende fil.
    """

    output_folder = Path(
        "tests_local"
    )

    output_folder.mkdir(
        exist_ok=True
    )

    output_path = (
        output_folder
        / filename
    )

    content = json.dumps(
        data,
        indent=4,
        ensure_ascii=False,
        default=str,
    )

    #
    # Anonymiser alt lige inden filen gemmes
    #

    content = anonymize_text(
        content
    )

    output_path.write_text(
        content,
        encoding="utf-8",
    )

    print()

    print(
        f"✅ Dump gemt: {output_path}"
    )