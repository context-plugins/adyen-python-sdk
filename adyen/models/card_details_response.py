from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .card_brand_details import CardBrandDetails, CardBrandDetailsDict


class CardDetailsResponse(SdkBaseModel):
    brands: Optional[list[CardBrandDetails]] = UNSET
    """The list of brands identified for the card."""

    funding_source: Optional[str] = Field(default=UNSET, alias="fundingSource")
    """The funding source of the card, for example **DEBIT**, **CREDIT**, or **PREPAID**."""

    is_card_commercial: Optional[bool] = Field(default=UNSET, alias="isCardCommercial")
    """Indicates if this is a commercial card or a consumer card. If **true**, it is a commercial card. If **false**, it
    is a consumer card."""

    issuing_country_code: Optional[str] = Field(default=UNSET, alias="issuingCountryCode")
    """The two-letter country code of the country where the card was issued."""


class CardDetailsResponseDict(TypedDict):
    brands: NotRequired[list[CardBrandDetailsDict]]
    funding_source: NotRequired[str]
    is_card_commercial: NotRequired[bool]
    issuing_country_code: NotRequired[str]
