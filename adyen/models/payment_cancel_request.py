from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .application_info import ApplicationInfo, ApplicationInfoDict


class PaymentCancelRequest(SdkBaseModel):
    application_info: Optional[ApplicationInfo] = Field(default=UNSET, alias="applicationInfo")
    """Information about your application. For more details, see `Building Adyen solutions
    <https://docs.adyen.com/development-resources/building-adyen-solutions>`__."""

    merchant_account: str = Field(alias="merchantAccount")
    """The merchant account that is used to process the payment."""

    reference: Optional[str] = UNSET
    """Your reference for the cancel request. Maximum length: 80 characters."""


class PaymentCancelRequestDict(TypedDict):
    application_info: NotRequired[ApplicationInfo | ApplicationInfoDict]
    merchant_account: str
    reference: NotRequired[str]
