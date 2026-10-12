from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .links11 import Links11, Links11Dict


class ConfirmPaymentResponse(SdkBaseModel):
    links: Links11
    """Contains redirection URLs to guide the user to the appropriate page, after a successful payment or a
    cancellation."""


class ConfirmPaymentResponseDict(TypedDict):
    links: Links11Dict
