from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .bank_account_info1 import BankAccountInfo1, BankAccountInfo1Dict
from .enums.type221 import Type221OrStr


class TransferInstrumentInfo(SdkBaseModel):
    bank_account: BankAccountInfo1 = Field(alias="bankAccount")
    """Contains information about the legal entity's bank account."""

    legal_entity_id: str = Field(alias="legalEntityId")
    """The unique identifier of the `legal entity
    <https://docs.adyen.com/api-explorer/legalentity/latest/post/legalEntities#responses-200-id>`__ that owns the
    transfer instrument."""

    type_: Type221OrStr = Field(alias="type")
    """The type of transfer instrument.

    Possible value: **bankAccount**."""


class TransferInstrumentInfoDict(TypedDict):
    bank_account: BankAccountInfo1 | BankAccountInfo1Dict
    legal_entity_id: str
    type_: Type221OrStr
