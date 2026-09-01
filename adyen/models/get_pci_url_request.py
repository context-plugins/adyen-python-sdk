from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class GetPciUrlRequest(SdkBaseModel):
    account_holder_code: str = Field(alias="accountHolderCode")
    """The account holder code you provided when you created the account holder."""

    return_url: Optional[str] = Field(default=UNSET, alias="returnUrl")
    """The URL where the account holder will be redirected back to after they fill out the questionnaire, or if their
    session times out. Maximum length of 500 characters."""


class GetPciUrlRequestDict(TypedDict):
    account_holder_code: str
    return_url: NotRequired[str]
