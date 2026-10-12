from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .bank_account_info1 import BankAccountInfo1, BankAccountInfo1Dict
from .capability_problem1 import CapabilityProblem1, CapabilityProblem1Dict
from .document_reference import DocumentReference, DocumentReferenceDict
from .enums.type221 import Type221OrStr
from .supporting_entity_capability import SupportingEntityCapability, SupportingEntityCapabilityDict


class TransferInstrument(SdkBaseModel):
    bank_account: BankAccountInfo1 = Field(alias="bankAccount")
    """Contains information about the legal entity's bank account."""

    capabilities: Optional[dict[str, SupportingEntityCapability]] = UNSET
    """List of capabilities for this transfer instrument."""

    document_details: Optional[list[DocumentReference]] = Field(default=UNSET, alias="documentDetails")
    """List of documents uploaded for the transfer instrument."""

    id: str
    """The unique identifier of the transfer instrument."""

    legal_entity_id: str = Field(alias="legalEntityId")
    """The unique identifier of the `legal entity
    <https://docs.adyen.com/api-explorer/legalentity/latest/post/legalEntities#responses-200-id>`__ that owns the
    transfer instrument."""

    problems: Optional[list[CapabilityProblem1]] = UNSET
    """The verification errors related to capabilities for this transfer instrument."""

    type_: Type221OrStr = Field(alias="type")
    """The type of transfer instrument.

    Possible value: **bankAccount**."""


class TransferInstrumentDict(TypedDict):
    bank_account: BankAccountInfo1Dict
    capabilities: NotRequired[dict[str, SupportingEntityCapabilityDict]]
    document_details: NotRequired[list[DocumentReferenceDict]]
    id: str
    legal_entity_id: str
    problems: NotRequired[list[CapabilityProblem1Dict]]
    type_: Type221OrStr
