from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .dynamic_offer import DynamicOffer, DynamicOfferDict


class GetDynamicOffersResponse(SdkBaseModel):
    dynamic_offers: list[DynamicOffer] = Field(alias="dynamicOffers")
    """Contains a list of available dynamic offers for the specified account holder."""


class GetDynamicOffersResponseDict(TypedDict):
    dynamic_offers: list[DynamicOfferDict]
