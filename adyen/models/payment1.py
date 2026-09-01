from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Payment1(SdkBaseModel):
    contactless_currency: Optional[str] = Field(default=UNSET, alias="contactlessCurrency")
    """The default currency for contactless payments on the payment terminal, in three-letter `ISO 4217
    <https://en.wikipedia.org/wiki/ISO_4217>`__ currency code format.

    Contact Adyen before you update this setting for the first time. To enable you to change the contactless currency,
    we first need to check if you meet the compliance requirements."""

    hide_minor_units_in_currencies: Optional[list[str]] = Field(default=UNSET, alias="hideMinorUnitsInCurrencies")
    """Hides the minor units for the listed `ISO currency codes <https://en.wikipedia.org/wiki/ISO_4217>`__."""


class Payment1Dict(TypedDict):
    contactless_currency: NotRequired[str]
    hide_minor_units_in_currencies: NotRequired[list[str]]
