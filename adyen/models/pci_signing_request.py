from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class PciSigningRequest(SdkBaseModel):
    pci_template_references: list[str] = Field(alias="pciTemplateReferences")
    """The array of Adyen-generated unique identifiers for the questionnaires."""

    signed_by: str = Field(alias="signedBy")
    """The `legal entity ID
    <https://docs.adyen.com/api-explorer/#/legalentity/latest/post/legalEntities__resParam_id>`__ of the individual who
    signs the PCI questionnaire."""


class PciSigningRequestDict(TypedDict):
    pci_template_references: list[str]
    signed_by: str
