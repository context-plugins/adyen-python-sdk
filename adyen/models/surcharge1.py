from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .configuration import Configuration, ConfigurationDict


class Surcharge1(SdkBaseModel):
    ask_confirmation: Optional[bool] = Field(default=UNSET, alias="askConfirmation")
    """Show the surcharge details on the terminal, so the shopper can confirm."""

    configurations: Optional[list[Configuration]] = UNSET
    """Surcharge fees or percentages for specific cards, funding sources (credit or debit), and currencies."""

    disclosure_on_present_card: Optional[bool] = Field(default=UNSET, alias="disclosureOnPresentCard")
    """Show the maximum surcharge rate to the shopper on the present card screen before they tap."""

    exclude_gratuity_from_surcharge: Optional[bool] = Field(default=UNSET, alias="excludeGratuityFromSurcharge")
    """Exclude the tip amount from the surcharge calculation."""


class Surcharge1Dict(TypedDict):
    ask_confirmation: NotRequired[bool]
    configurations: NotRequired[list[ConfigurationDict]]
    disclosure_on_present_card: NotRequired[bool]
    exclude_gratuity_from_surcharge: NotRequired[bool]
