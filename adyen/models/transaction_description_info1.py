from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.type8 import Type8OrStr


class TransactionDescriptionInfo1(SdkBaseModel):
    """Information regarding the transaction description.
    > You cannot configure the transaction description in the test environment."""

    doing_business_as_name: Optional[str] = Field(default=UNSET, alias="doingBusinessAsName")
    """The text to be shown on the shopper's bank statement.
     We recommend sending a maximum of 22 characters, otherwise banks might truncate the string.
     Allowed characters: **a-z**, **A-Z**, **0-9**, spaces, and special characters **. , ' _ - ? + * /**."""

    type_: Optional[Type8OrStr] = Field(default=UNSET, alias="type")
    """The type of transaction description you want to use:
    - **fixed**: The transaction description set in this request is used for all payments with this payment method.
    - **append**: The transaction description set in this request is used as a base for all payments with this payment
        method. The `transaction description set in the request to process the payment
        <https://docs.adyen.com/api-explorer/Checkout/70/post/sessions#request-shopperStatement>`__ is appended to this
        base description. Note that if the combined length exceeds 22 characters, banks may truncate the string.
    - **dynamic**: Only the `transaction description set in the request to process the payment
        <https://docs.adyen.com/api-explorer/Checkout/70/post/sessions#request-shopperStatement>`__ is used for payments
        with this payment method."""


class TransactionDescriptionInfo1Dict(TypedDict):
    doing_business_as_name: NotRequired[str]
    type_: NotRequired[Type8OrStr]
