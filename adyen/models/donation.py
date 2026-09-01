from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Donation(SdkBaseModel):
    currency: str
    """The three-character `ISO currency code <https://docs.adyen.com/development-resources/currency-codes/>`__."""

    donation_type: Optional[str] = Field(default=UNSET, alias="donationType")
    """The `type of donation <https://docs.adyen.com/online-payments/donations/#donation-types>`__.

    Possible values:
    * **roundup**: a donation where the original transaction amount is rounded up as a donation.
    * **fixedAmounts**: a donation where you show fixed donations amounts that the shopper can select from."""

    max_roundup_amount: Optional[int] = Field(default=UNSET, alias="maxRoundupAmount")
    """The maximum amount a transaction can be rounded up to make a donation. This field is only present when
    ``donationType`` is **roundup**."""

    type_: str = Field(alias="type")
    """The `type of donation <https://docs.adyen.com/online-payments/donations/#donation-types>`__.

    Possible values:
    * **roundup**: a donation where the original transaction amount is rounded up as a donation.
    * **fixedAmounts**: a donation where you show fixed donation amounts that the shopper can select from."""

    values: Optional[list[int]] = UNSET
    """The fixed donation amounts in `minor units
    <https://docs.adyen.com/development-resources/currency-codes//#minor-units>`__. This field is only present when
    ``donationType`` is **fixedAmounts**."""


class DonationDict(TypedDict):
    currency: str
    donation_type: NotRequired[str]
    max_roundup_amount: NotRequired[int]
    type_: str
    values: NotRequired[list[int]]
