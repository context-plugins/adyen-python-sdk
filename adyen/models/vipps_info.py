from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class VippsInfo(SdkBaseModel):
    logo: str
    """Vipps logo. Format: Base64-encoded string."""

    subscription_cancel_url: Optional[str] = Field(default=UNSET, alias="subscriptionCancelUrl")
    """Vipps subscription cancel url (required in case of `recurring payments
    <https://docs.adyen.com/online-payments/tokenization>`__)"""


class VippsInfoDict(TypedDict):
    logo: str
    subscription_cancel_url: NotRequired[str]
