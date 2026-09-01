from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SaleSoftware(SdkBaseModel):
    """Information related to the software of the Sale System which manages the NEXO Sale to POI protocol."""

    manufacturer_id: str = Field(alias="ManufacturerID")
    """Identification of the Manufacturer."""

    application_name: str = Field(alias="ApplicationName")
    """Name of the software product."""

    software_version: str = Field(alias="SoftwareVersion")
    """Version of the software product."""

    certification_code: str = Field(alias="CertificationCode")
    """Certification code of the software which manages the Sale to POI protocol."""


class SaleSoftwareDict(TypedDict):
    manufacturer_id: str
    application_name: str
    software_version: str
    certification_code: str
