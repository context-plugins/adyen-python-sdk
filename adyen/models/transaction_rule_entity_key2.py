from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class TransactionRuleEntityKey2(SdkBaseModel):
    """The type and unique identifier of the resource to which the rule applies."""

    entity_reference: Optional[str] = Field(default=UNSET, alias="entityReference")
    """The unique identifier of the resource."""

    entity_type: Optional[str] = Field(default=UNSET, alias="entityType")
    """The type of resource.

    Possible values: **balancePlatform**, **paymentInstrumentGroup**, **accountHolder**, **balanceAccount**, or
    **paymentInstrument**."""


class TransactionRuleEntityKey2Dict(TypedDict):
    entity_reference: NotRequired[str]
    entity_type: NotRequired[str]
