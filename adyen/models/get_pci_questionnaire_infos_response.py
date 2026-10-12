from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .pci_document_info import PciDocumentInfo, PciDocumentInfoDict


class GetPciQuestionnaireInfosResponse(SdkBaseModel):
    data: Optional[list[PciDocumentInfo]] = UNSET
    """Information about the signed PCI questionnaires."""


class GetPciQuestionnaireInfosResponseDict(TypedDict):
    data: NotRequired[list[PciDocumentInfoDict]]
