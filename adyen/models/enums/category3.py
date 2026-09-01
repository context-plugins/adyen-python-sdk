from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Category3(str, Enum):
    """The category of the transfer.

    Possible values:

     - **bank**: A transfer involving a `transfer instrument
            <https://docs.adyen.com/api-explorer/legalentity/latest/post/transferInstruments#responses-200-id>`__ or a
            bank account.

    - **card**: A transfer involving a third-party card.

    - **internal**: A transfer between `balance accounts
        <https://docs.adyen.com/api-explorer/balanceplatform/latest/post/balanceAccounts#responses-200-id>`__ within
        your platform.

    - **issuedCard**: A transfer initiated by an Adyen-issued card.

    - **platformPayment**: Funds movements related to payments that are acquired for your users.

    - **topUp**: An incoming transfer initiated by your user to top up their balance account."""

    BANK = "bank"
    CARD = "card"
    INTERNAL = "internal"
    ISSUED_CARD = "issuedCard"
    PLATFORM_PAYMENT = "platformPayment"
    TOP_UP = "topUp"

    __str__ = str.__str__


Category3OrStr: TypeAlias = Annotated[Category3 | str, open_enum_validator(Category3)]
