from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .collect_information1 import CollectInformation1, CollectInformation1Dict
from .show_pages2 import ShowPages2, ShowPages2Dict


class GetOnboardingUrlRequest(SdkBaseModel):
    account_holder_code: str = Field(alias="accountHolderCode")
    """The account holder code you provided when you created the account holder."""

    collect_information: Optional[CollectInformation1] = Field(default=UNSET, alias="collectInformation")
    """Contains indicators whether the page should only collect information for specific `KYC checks
    <https://docs.adyen.com/classic-platforms/verification-checks>`__. By default, the page collects information for all
    KYC checks that apply to the `legal entity type
    <https://docs.adyen.com/classic-platforms/account-holders-and-accounts#legal-entity-types>`__."""

    edit_mode: Optional[bool] = Field(default=UNSET, alias="editMode")
    """Indicates if editing checks is allowed even if all the checks have passed."""

    mobile_o_auth_callback_url: Optional[str] = Field(default=UNSET, alias="mobileOAuthCallbackUrl")
    """The URL to which the account holder is redirected after completing an OAuth authentication with a bank through
    Trustly/PayMyBank."""

    platform_name: Optional[str] = Field(default=UNSET, alias="platformName")
    """The platform name which will show up in the welcome page."""

    return_url: Optional[str] = Field(default=UNSET, alias="returnUrl")
    """The URL where the account holder will be redirected back to after they complete the onboarding, or if their
    session times out. Maximum length of 500 characters. If you don't provide this, the account holder will be
    redirected back to the default return URL configured in your platform account."""

    shopper_locale: Optional[str] = Field(default=UNSET, alias="shopperLocale")
    """The language to be used in the page, specified by a combination of a language and country code. For example,
    **pt-BR**.

    If not specified in the request or if the language is not supported, the page uses the browser language. If the
    browser language is not supported, the page uses **en-US** by default.

    For a list of supported languages, refer to `Change the page language
    <https://docs.adyen.com/classic-platforms/hosted-onboarding-page/customize-experience#change-page-language>`__."""

    show_pages: Optional[ShowPages2] = Field(default=UNSET, alias="showPages")
    """Contains indicators whether specific pages must be shown to the account holder."""


class GetOnboardingUrlRequestDict(TypedDict):
    account_holder_code: str
    collect_information: NotRequired[CollectInformation1Dict]
    edit_mode: NotRequired[bool]
    mobile_o_auth_callback_url: NotRequired[str]
    platform_name: NotRequired[str]
    return_url: NotRequired[str]
    shopper_locale: NotRequired[str]
    show_pages: NotRequired[ShowPages2Dict]
