from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.account_verification_country2 import AccountVerificationCountry2OrStr


class AccountVerificationRoutesRequest(SdkBaseModel):
    country: AccountVerificationCountry2OrStr
    """The location where the third-party individual's bank account is registered. Adyen uses this information to
    determine an available open banking provider, and to configure the open banking flow for that respective
    location."""

    locale: Optional[str] = UNSET
    """The language to use in the open banking flow UI, specified by a combination of a two-letter `ISO 639-1
    <https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes>`__ language code and an `ISO 3166-1 alpha-2
    <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2>`__ country code.

    This information is used to configure the open banking flow with the same language for a consistent user experience.

    Default value: **en-US**"""

    redirect_url: str = Field(alias="redirectUrl")
    """The URL where Adyen redirects the third-party individual after they complete the open banking flow."""

    state: Optional[str] = UNSET
    """A value that helps you identify the request in callback handling. You can generate this value on a per-session
    basis to protect the callback against Cross-Site Request Forgery (CSRF) attacks. This value must be composed of
    characters that can be successfully URL-encoded."""


class AccountVerificationRoutesRequestDict(TypedDict):
    country: AccountVerificationCountry2OrStr
    locale: NotRequired[str]
    redirect_url: str
    state: NotRequired[str]
