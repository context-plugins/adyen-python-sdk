from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class MandateUpdate(SdkBaseModel):
    payment_instrument_id: OptionalNullable[str] = Field(default=UNSET, alias="paymentInstrumentId")
    """The unique identifier of the payment instrument linked to the mandate."""


class MandateUpdateDict(TypedDict):
    payment_instrument_id: NotRequired[str | None]
