from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .track_data import TrackData, TrackDataDict


class SensitiveCardData(SdkBaseModel):
    """This data structure could be CMS protected (EnvelopedData). In this case the data structure SensitiveCardData is
    replaced by the data structure ProtectedCardData of type ContentInformationType. When this data is protected, the
    exact content is unknown by the Sale System, and might include all the information which are required by an external
    backup POI Server to make a batch payment transaction in case of problem with the POI System. Sensitive information
    related to the payment card, entered or read by the Sale System."""

    pan: Optional[int] = Field(default=UNSET, alias="PAN")
    """Primary Account Number."""

    card_seq_numb: Optional[int] = Field(default=UNSET, alias="CardSeqNumb")
    """Card Sequence Number. If EntryMode is File, Keyed, or Manual."""

    expiry_date: Optional[int] = Field(default=UNSET, alias="ExpiryDate")
    """Date after which the card cannot be used. If EntryMode is File."""

    track_data: Optional[list[TrackData]] = Field(default=UNSET, alias="TrackData")
    """Magnetic track or magnetic ink characters line. If EntryMode is MagStripe or RFID ."""


class SensitiveCardDataDict(TypedDict):
    pan: NotRequired[int]
    card_seq_numb: NotRequired[int]
    expiry_date: NotRequired[int]
    track_data: NotRequired[list[TrackDataDict]]
