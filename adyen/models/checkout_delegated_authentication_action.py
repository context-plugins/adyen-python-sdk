from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CheckoutDelegatedAuthenticationAction(SdkBaseModel):
    authorisation_token: Optional[str] = Field(default=UNSET, alias="authorisationToken")
    """A token needed to authorise a payment."""

    payment_data: Optional[str] = Field(default=UNSET, alias="paymentData")
    """Encoded payment data."""

    payment_method_type: Optional[str] = Field(default=UNSET, alias="paymentMethodType")
    """Specifies the payment method."""

    token: Optional[str] = UNSET
    """A token to pass to the delegatedAuthentication component."""

    type_: Literal["delegatedAuthentication"] = Field(default="delegatedAuthentication", alias="type")
    """**delegatedAuthentication**"""

    url: Optional[str] = UNSET
    """Specifies the URL to redirect to."""


class CheckoutDelegatedAuthenticationActionDict(TypedDict):
    authorisation_token: NotRequired[str]
    payment_data: NotRequired[str]
    payment_method_type: NotRequired[str]
    token: NotRequired[str]
    type_: NotRequired[Literal["delegatedAuthentication"]]
    url: NotRequired[str]
