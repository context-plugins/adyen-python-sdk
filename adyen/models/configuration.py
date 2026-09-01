from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .currency import Currency, CurrencyDict


class Configuration(SdkBaseModel):
    brand: str
    """Payment method, like **eftpos_australia** or **mc**. See the `possible values
    <https://docs.adyen.com/development-resources/paymentmethodvariant#management-api>`__."""

    commercial: Optional[bool] = UNSET
    """Set to **true** to apply surcharges only to commercial/business cards."""

    country: Optional[list[str]] = UNSET
    """The country/region of the card issuer. If used, the surcharge settings only apply to the card issued in that
    country/region."""

    currencies: list[Currency]
    """Currency and percentage or amount of the surcharge."""

    sources: Optional[list[str]] = UNSET
    """Funding source. Possible values:
    * **Credit**
    * **Debit**"""


class ConfigurationDict(TypedDict):
    brand: str
    commercial: NotRequired[bool]
    country: NotRequired[list[str]]
    currencies: list[Currency | CurrencyDict]
    sources: NotRequired[list[str]]
