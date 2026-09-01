from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class SupportedCardTypes(SdkBaseModel):
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


class SupportedCardTypesDict(TypedDict):
    credit: NotRequired[bool]
    debit: NotRequired[bool]
    deferred_debit: NotRequired[bool]
    prepaid: NotRequired[bool]
    unknown: NotRequired[bool]
