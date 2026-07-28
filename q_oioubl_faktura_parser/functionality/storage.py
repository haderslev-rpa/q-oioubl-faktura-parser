"""
Læsning af filer fra AOS Storage.

Denne klasse (skabelon for objekter)
har kun ét ansvar:

At hente filer fra SMB share
direkte til memory (RAM).
"""

from automation_server_client import (
    AutomationServer,
    Credential,
)

import smbclient


class StorageClient:
    """
    Client (objekt som taler med storage).
    """

    CREDENTIAL_NAME = "DIRXKFP"

    SERVER = (
        "dk-p365-haaos01.prisme-365.dk"
    )

    def __init__(self):
        """
        Hent credentials
        fra Automation Server.
        """

        AutomationServer.from_environment()

        credential = (
            Credential.get_credential(
                self.CREDENTIAL_NAME
            )
        )

        self.username = (
            credential.username
        )

        self.password = (
            credential.password
        )

    def read_text(
        self,
        file_path: str,
    ) -> str:
        """
        Læser fil direkte
        til memory (RAM).

        Args:
            file_path:
                Fuld UNC sti.

        Returns:
            Filens indhold som tekst.
        """

        smbclient.register_session(
            server=self.SERVER,
            username=self.username,
            password=self.password,
        )

        with smbclient.open_file(
            file_path,
            mode="r",
            encoding="utf-8",
        ) as file:

            return file.read()