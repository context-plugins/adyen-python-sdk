from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class SupportedCardTypes2(SdkBaseModel):
    """The type of card for which the terminal accepts store-and-forward payments. You can specify multiple card
    types."""

    credit: Optional[bool] = UNSET
    """Set to **true** to accept credit cards."""

    debit: Optional[bool] = UNSET
    """Set to **true** to accept debit cards."""

    deferred_debit: Optional[bool] = Field(default=UNSET, alias="deferredDebit")
    """Set to **true** to accept cards that allow deferred debit."""

    prepaid: Optional[bool] = UNSET
    """Set to **true** to accept prepaid cards."""

    unknown: Optional[bool] = UNSET
    """Set to **true** to accept card types for which the terminal can't determine the funding source while offline."""


class SupportedCardTypes2Dict(TypedDict):
    credit: NotRequired[bool]
    debit: NotRequired[bool]
    deferred_debit: NotRequired[bool]
    prepaid: NotRequired[bool]
    unknown: NotRequired[bool]
