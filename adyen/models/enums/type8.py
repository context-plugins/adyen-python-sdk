from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type8(str, Enum):
    """The type of transaction description you want to use:
    - **fixed**: The transaction description set in this request is used for all payments with this payment method.
    - **append**: The transaction description set in this request is used as a base for all payments with this payment
        method. The `transaction description set in the request to process the payment
        <https://docs.adyen.com/api-explorer/Checkout/70/post/sessions#request-shopperStatement>`__ is appended to this
        base description. Note that if the combined length exceeds 22 characters, banks may truncate the string.
    - **dynamic**: Only the `transaction description set in the request to process the payment
        <https://docs.adyen.com/api-explorer/Checkout/70/post/sessions#request-shopperStatement>`__ is used for payments
        with this payment method."""

    APPEND = "append"
    DYNAMIC = "dynamic"
    FIXED = "fixed"

    __str__ = str.__str__


Type8OrStr: TypeAlias = Annotated[Type8 | str, open_enum_validator(Type8)]
