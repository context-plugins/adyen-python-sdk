from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .onboarding_link_settings2 import OnboardingLinkSettings2, OnboardingLinkSettings2Dict


class OnboardingLinkInfo(SdkBaseModel):
    locale: Optional[str] = UNSET
    """The language that will be used for the page, specified by a combination of two letter `ISO 639-1
    <https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes>`__ language and `ISO 3166-1 alpha-2
    <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2>`__ country codes. See possible valuesfor `marketplaces
    <https://docs.adyen.com/marketplaces/onboard-users/hosted#supported-languages>`__ or `platforms
    <https://docs.adyen.com/platforms/onboard-users/hosted#supported-languages>`__.

    If not specified in the request or if the language is not supported, the page uses the browser language. If the
    browser language is not supported, the page uses **en-US** by default."""

    redirect_url: Optional[str] = Field(default=UNSET, alias="redirectUrl")
    """The URL where the user is redirected after they complete hosted onboarding."""

    settings: Optional[OnboardingLinkSettings2] = UNSET
    """Key-value pairs indicating the settings for the hosted onboarding page. The key represents a specific setting."""

    theme_id: Optional[str] = Field(default=UNSET, alias="themeId")
    """The unique identifier of the hosted onboarding theme."""


class OnboardingLinkInfoDict(TypedDict):
    locale: NotRequired[str]
    redirect_url: NotRequired[str]
    settings: NotRequired[OnboardingLinkSettings2 | OnboardingLinkSettings2Dict]
    theme_id: NotRequired[str]
