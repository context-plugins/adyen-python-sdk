from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class TopUpCounterparty1(SdkBaseModel):
    """The details about the counterparty that is funding the top-up."""

    transfer_instrument_id: str = Field(alias="transferInstrumentId")
    """The unique identifier of the `transfer instrument
    <https://docs.adyen.com/api-explorer/legalentity/latest/post/transferInstruments#responses-200-id>`__ that is
    funding the top-up."""


class TopUpCounterparty1Dict(TypedDict):
    transfer_instrument_id: str
