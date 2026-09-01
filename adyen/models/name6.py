from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Name6(SdkBaseModel):
    status: str
    """Set to **requested** to request a `name validation
    <https://docs.adyen.com/payment-methods/cards/name-validation>`__ to verify if the cardholder name provided by the
    shopper matches the cardholder name on file at the issuing bank."""


class Name6Dict(TypedDict):
    status: str
