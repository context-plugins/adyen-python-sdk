from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ProfileRegistrationRequest(SdkBaseModel):
    account_holder_id: str = Field(alias="accountHolderId")
    """The unique identifier of the account holder."""

    payment_instrument_ids: list[str] = Field(alias="paymentInstrumentIds")
    """The unique identifiers of the payment instruments to be associated with the iDEAL profile."""


class ProfileRegistrationRequestDict(TypedDict):
    account_holder_id: str
    payment_instrument_ids: list[str]
