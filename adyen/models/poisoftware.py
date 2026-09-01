from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Poisoftware(SdkBaseModel):
    """Information related to the software of the POI System which manages the Sale to POI protocol. In a session allows
    identifying the product features of a POI System."""

    manufacturer_id: str = Field(alias="ManufacturerID")
    """Identification of the Manufacturer. Sent in the Login Request (Response) to identify the Sale System (POI System)
    manufacturer during the session."""

    application_name: str = Field(alias="ApplicationName")
    """Name of the software product. Sent in the Login Request (Response) to identify the Sale System (POI System)
    product name during the session."""

    software_version: str = Field(alias="SoftwareVersion")
    """Version of the software product. Sent in the Login Request (Response) to identify the version of the Sale System
    (POI System) product software during the session."""

    certification_code: str = Field(alias="CertificationCode")
    """Certification code of the software which manages the Sale to POI protocol. Sent in the Login Request (Response)
    to get the certification code of the Sale System (POI System) product software. This code can be a software checksum
    or any number associated with the software."""


class PoisoftwareDict(TypedDict):
    manufacturer_id: str
    application_name: str
    software_version: str
    certification_code: str
