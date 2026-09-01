from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class KlarnaNetwork(SdkBaseModel):
    checkout_attempt_id: Optional[str] = Field(default=UNSET, alias="checkoutAttemptId")
    """The checkout attempt identifier."""

    klarna_network_data: Optional[str] = Field(default=UNSET, alias="klarnaNetworkData")
    """A string containing a structured JSON object. This is a passthrough field used to enable custom features or data
    exchange with Klarna."""

    klarna_network_session_token: Optional[str] = Field(default=UNSET, alias="klarnaNetworkSessionToken")
    """The token obtained from the Klarna SDK during an Express Checkout flow."""

    recurring_detail_reference: Optional[str] = Field(default=UNSET, alias="recurringDetailReference")
    """This is the ``recurringDetailReference`` returned in the response when you created the token."""

    sdk_data: Optional[str] = Field(default=UNSET, alias="sdkData")
    """Base64-encoded JSON object containing SDK related parameters required by the SDK"""

    stored_payment_method_id: Optional[str] = Field(default=UNSET, alias="storedPaymentMethodId")
    """This is the ``recurringDetailReference`` returned in the response when you created the token."""

    type_: Literal["klarna_network"] = Field(default="klarna_network", alias="type")
    """**klarna_network**"""


class KlarnaNetworkDict(TypedDict):
    checkout_attempt_id: NotRequired[str]
    klarna_network_data: NotRequired[str]
    klarna_network_session_token: NotRequired[str]
    recurring_detail_reference: NotRequired[str]
    sdk_data: NotRequired[str]
    stored_payment_method_id: NotRequired[str]
    type_: NotRequired[Literal["klarna_network"]]
