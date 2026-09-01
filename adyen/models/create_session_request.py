from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CreateSessionRequest(SdkBaseModel):
    merchant_account: str = Field(alias="merchantAccount")
    """The unique identifier of your merchant account."""

    setup_token: str = Field(alias="setupToken")
    """The setup token provided by the POS Mobile SDK.
    - When using the Android POS Mobile SDK, obtain the token through the
        ``AuthenticationService.authenticate(setupToken)`` callback of ``AuthenticationService``.
    - When using the iOS POS Mobile SDK, obtain the token through the ``PaymentServiceDelegate.register(with:)``
        callback of ``PaymentServiceDelegate``."""

    store: Optional[str] = UNSET
    """The unique identifier of the store that you want to process transactions for."""


class CreateSessionRequestDict(TypedDict):
    merchant_account: str
    setup_token: str
    store: NotRequired[str]
