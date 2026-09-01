from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Contract(str, Enum):
    """The type of recurring contract to be used. Possible values:
    * ``ONECLICK`` – Payment details can be used to initiate a one-click payment, where the shopper enters the `card
        security code (CVC/CVV)
        <https://docs.adyen.com/payments-fundamentals/payment-glossary#card-security-code-cvc-cvv-cid>`__.
    * ``RECURRING`` – Payment details can be used without the card security code to initiate `card-not-present
        transactions <https://docs.adyen.com/payments-fundamentals/payment-glossary#card-not-present-cnp>`__.
    * ``ONECLICK,RECURRING`` – Payment details can be used regardless of whether the shopper is on your site or not.
    * ``PAYOUT`` – Payment details can be used to `make a payout
        <https://docs.adyen.com/online-payments/online-payouts>`__.
    * ``EXTERNAL`` - Use this when you store payment details and send the raw card number or network token directly in
        your API request."""

    ONECLICK = "ONECLICK"
    ONECLICK_RECURRING = "ONECLICK,RECURRING"
    RECURRING = "RECURRING"
    PAYOUT = "PAYOUT"
    EXTERNAL = "EXTERNAL"

    __str__ = str.__str__


ContractOrStr: TypeAlias = Annotated[Contract | str, open_enum_validator(Contract)]
