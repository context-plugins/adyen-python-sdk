from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class PciSigningResponse(SdkBaseModel):
    pci_questionnaire_ids: Optional[list[str]] = Field(default=UNSET, alias="pciQuestionnaireIds")
    """The unique identifiers of the signed PCI documents."""

    signed_by: Optional[str] = Field(default=UNSET, alias="signedBy")
    """The `legal entity ID
    <https://docs.adyen.com/api-explorer/#/legalentity/latest/post/legalEntities__resParam_id>`__ of the individual who
    signed the PCI questionnaire."""


class PciSigningResponseDict(TypedDict):
    pci_questionnaire_ids: NotRequired[list[str]]
    signed_by: NotRequired[str]
