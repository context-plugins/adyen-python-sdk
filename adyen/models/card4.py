from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .card_identification3 import CardIdentification3, CardIdentification3Dict
from .party_identification1 import PartyIdentification1, PartyIdentification1Dict


class Card4(SdkBaseModel):
    card_holder: PartyIdentification1 = Field(alias="cardHolder")
    """Contains information about the cardholder."""

    card_identification: CardIdentification3 = Field(alias="cardIdentification")
    """Contains the identification details of the card."""


class Card4Dict(TypedDict):
    card_holder: PartyIdentification1 | PartyIdentification1Dict
    card_identification: CardIdentification3 | CardIdentification3Dict
