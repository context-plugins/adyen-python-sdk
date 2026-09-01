from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class PaymentInstrumentGroup(SdkBaseModel):
    balance_platform: str = Field(alias="balancePlatform")
    """The unique identifier of the `balance platform
    <https://docs.adyen.com/api-explorer/#/balanceplatform/latest/get/balancePlatforms/{id}__queryParam_id>`__ to which
    the payment instrument group belongs."""

    description: Optional[str] = UNSET
    """Your description for the payment instrument group."""

    id: Optional[str] = UNSET
    """The unique identifier of the payment instrument group."""

    properties: Optional[dict[str, str]] = UNSET
    """Properties of the payment instrument group."""

    reference: Optional[str] = UNSET
    """Your reference for the payment instrument group."""

    tx_variant: str = Field(alias="txVariant")
    """The tx variant of the payment instrument group."""


class PaymentInstrumentGroupDict(TypedDict):
    balance_platform: str
    description: NotRequired[str]
    id: NotRequired[str]
    properties: NotRequired[dict[str, str]]
    reference: NotRequired[str]
    tx_variant: str
