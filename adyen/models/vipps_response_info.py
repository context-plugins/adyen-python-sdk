from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class VippsResponseInfo(SdkBaseModel):
    logo: Optional[str] = UNSET
    """Vipps logo. Format: Base64-encoded string."""

    subscription_cancel_url: Optional[str] = Field(default=UNSET, alias="subscriptionCancelUrl")
    """Vipps subscription cancel url (required in case of `recurring payments
    <https://docs.adyen.com/online-payments/tokenization>`__)"""


class VippsResponseInfoDict(TypedDict):
    logo: NotRequired[str]
    subscription_cancel_url: NotRequired[str]
