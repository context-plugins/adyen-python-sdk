from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .onboarding_theme import OnboardingTheme, OnboardingThemeDict


class OnboardingThemes(SdkBaseModel):
    next: Optional[str] = UNSET
    """The next page. Only present if there is a next page."""

    previous: Optional[str] = UNSET
    """The previous page. Only present if there is a previous page."""

    themes: list[OnboardingTheme]
    """List of onboarding themes."""


class OnboardingThemesDict(TypedDict):
    next: NotRequired[str]
    previous: NotRequired[str]
    themes: list[OnboardingThemeDict]
