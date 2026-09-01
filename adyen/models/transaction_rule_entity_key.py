from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class TransactionRuleEntityKey(SdkBaseModel):
    entity_reference: Optional[str] = Field(default=UNSET, alias="entityReference")
    """The unique identifier of the resource."""

    entity_type: Optional[str] = Field(default=UNSET, alias="entityType")
    """The type of resource.

    Possible values: **balancePlatform**, **paymentInstrumentGroup**, **accountHolder**, **balanceAccount**, or
    **paymentInstrument**."""


class TransactionRuleEntityKeyDict(TypedDict):
    entity_reference: NotRequired[str]
    entity_type: NotRequired[str]
