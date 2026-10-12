from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class PaymentInstrumentResource(SdkBaseModel):
    """All Of Resource, PaymentInstrumentResource."""

    type_: Optional[str] = Field(default=UNSET, alias="type")
    payment_instrument_id: str = Field(alias="paymentInstrumentId")


class PaymentInstrumentResourceDict(TypedDict):
    type_: NotRequired[str]
    payment_instrument_id: str
