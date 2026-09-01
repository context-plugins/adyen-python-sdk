from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .grant_offer import GrantOffer, GrantOfferDict


class GrantOffers(SdkBaseModel):
    grant_offers: list[GrantOffer] = Field(alias="grantOffers")
    """A list of available grant offers."""


class GrantOffersDict(TypedDict):
    grant_offers: list[GrantOffer | GrantOfferDict]
