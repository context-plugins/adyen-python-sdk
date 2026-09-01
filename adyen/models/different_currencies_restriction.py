from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class DifferentCurrenciesRestriction(SdkBaseModel):
    operation: str
    """Defines how the condition must be evaluated."""

    value: Optional[bool] = UNSET
    """Checks the currency of the payment against the currency of the payment instrument.

    Possible values:

    - **true**: The currency of the payment is different from the currency of the payment instrument.

    - **false**: The currencies are the same."""


class DifferentCurrenciesRestrictionDict(TypedDict):
    operation: str
    value: NotRequired[bool]
