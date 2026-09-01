from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Gratuity(SdkBaseModel):
    allow_custom_amount: Optional[bool] = Field(default=UNSET, alias="allowCustomAmount")
    """Indicates whether one of the predefined tipping options is to let the shopper enter a custom tip. If **true**,
    only three of the other options defined in ``predefinedTipEntries`` are shown."""

    currency: Optional[str] = UNSET
    """The currency that the tipping settings apply to."""

    predefined_tip_entries: Optional[list[str]] = Field(default=UNSET, alias="predefinedTipEntries")
    """Tipping options the shopper can choose from if ``usePredefinedTipEntries`` is **true**. The maximum number of
    predefined options is four, or three plus the option to enter a custom tip. The options can be a mix of:

    - A percentage of the transaction amount. Example: **5%**
    - A tip amount in `minor units <https://docs.adyen.com/development-resources/currency-codes>`__. Example: **500**
        for a EUR 5 tip."""

    use_predefined_tip_entries: Optional[bool] = Field(default=UNSET, alias="usePredefinedTipEntries")
    """Indicates whether the terminal shows a prompt to enter a tip (**false**), or predefined tipping options to choose
    from (**true**)."""


class GratuityDict(TypedDict):
    allow_custom_amount: NotRequired[bool]
    currency: NotRequired[str]
    predefined_tip_entries: NotRequired[list[str]]
    use_predefined_tip_entries: NotRequired[bool]
