from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .track_data import TrackData, TrackDataDict


class SensitiveCardData1(SdkBaseModel):
    """Sensitive information related to the payment card, entered or read by the Sale System. If structure non empty and
    unprotected."""

    pan: Optional[int] = Field(default=UNSET, alias="PAN")
    """Primary Account Number."""

    card_seq_numb: Optional[int] = Field(default=UNSET, alias="CardSeqNumb")
    """Card Sequence Number. If EntryMode is File, Keyed, or Manual."""

    expiry_date: Optional[int] = Field(default=UNSET, alias="ExpiryDate")
    """Date after which the card cannot be used. If EntryMode is File."""

    track_data: Optional[list[TrackData]] = Field(default=UNSET, alias="TrackData")
    """Magnetic track or magnetic ink characters line. If EntryMode is MagStripe or RFID ."""


class SensitiveCardData1Dict(TypedDict):
    pan: NotRequired[int]
    card_seq_numb: NotRequired[int]
    expiry_date: NotRequired[int]
    track_data: NotRequired[list[TrackDataDict]]
