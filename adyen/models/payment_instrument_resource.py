from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel


class PaymentInstrumentResource(SdkBaseModel):
    """All Of Resource, PaymentInstrumentResource."""

    type_: Literal["paymentInstrument"] = Field(default="paymentInstrument", alias="type")

    payment_instrument_id: str = Field(alias="paymentInstrumentId")


class PaymentInstrumentResourceDict(TypedDict):
    type_: NotRequired[Literal["paymentInstrument"]]
    payment_instrument_id: str
