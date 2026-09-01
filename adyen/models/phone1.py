from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Phone1(SdkBaseModel):
    """The mobile phone number provided by the cardholder. The phone number must consist of a country code, followed by
    the number. If the value you provide does not follow the guidelines, we do not submit it for authentication.
    > Required for Visa and JCB transactions that require 3D Secure 2 authentication, if you did not include the
        ``shopperEmail``, and did not send the shopper's phone number in ``telephoneNumber``."""

    cc: Optional[str] = UNSET
    """Country code. Length: 1–3 digits."""

    subscriber: Optional[str] = UNSET
    """Subscriber number. Length: 4-15 digits."""


class Phone1Dict(TypedDict):
    cc: NotRequired[str]
    subscriber: NotRequired[str]
