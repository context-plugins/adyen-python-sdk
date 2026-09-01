from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class SplitAmount(SdkBaseModel):
    """The amount of the split item.

    * Required for all split types in the `Classic Platforms integration <https://docs.adyen.com/classic-platforms>`__.
    * Required if ``type`` is **BalanceAccount**, **Commission**, **Surcharge**, **Default**, or **VAT** in your
        `Balance Platform <https://docs.adyen.com/adyen-for-platforms-model>`__ integration., The amount of the split
        item.

    * Required for all split types in the `Classic Platforms integration <https://docs.adyen.com/classic-platforms>`__.
    * Required if ``type`` is **BalanceAccount**, **Commission**, **Default**, or **VAT** in your `Balance Platform
        <https://docs.adyen.com/adyen-for-platforms-model>`__ integration."""

    currency: Optional[str] = UNSET
    """The three-character `ISO currency code <https://docs.adyen.com/development-resources/currency-codes>`__. By
    default, this is the original payment currency."""

    value: int
    """The value of the split amount, in `minor units
    <https://docs.adyen.com/development-resources/currency-codes>`__."""


class SplitAmountDict(TypedDict):
    currency: NotRequired[str]
    value: int
