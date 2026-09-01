from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .enums.token_requested_type1 import TokenRequestedType1OrStr


class PaymentToken1(SdkBaseModel):
    """Surrogate of the PAN (Primary Account Number) of the payment card to identify the payment mean of the customer.
    It allows, for a merchant, to identify the customer. Restriction of product payable by a card."""

    token_requested_type: TokenRequestedType1OrStr = Field(alias="TokenRequestedType")
    """Type of token replacing the PAN of a payment card to identify the payment
     mean of the customer. It allows, for a merchant, to use a token for a transaction
     only or for a longer period.
    Possible values:
    * **Customer**
    * **Transaction**"""

    token_value: str = Field(alias="TokenValue")
    """Payment token replacing the PAN of the payment card to identify the payment
     mean of the customer."""

    expiry_date_time: Optional[RFC3339DateTime] = Field(default=UNSET, alias="ExpiryDateTime")
    """Expiry date and time. Limits the validity of a payment token."""


class PaymentToken1Dict(TypedDict):
    token_requested_type: TokenRequestedType1OrStr
    token_value: str
    expiry_date_time: NotRequired[RFC3339DateTime]
