from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CountriesRestriction1(SdkBaseModel):
    """List of countries and the operation.

    Supported operations: **anyMatch**, **noneMatch**."""

    operation: str
    """Defines how the condition must be evaluated."""

    value: Optional[list[str]] = UNSET
    """List of two-character `ISO 3166-1 alpha-2 <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2>`__ country codes."""


class CountriesRestriction1Dict(TypedDict):
    operation: str
    value: NotRequired[list[str]]
