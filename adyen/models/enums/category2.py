from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Category2(str, Enum):
    """The type of transfer.

     Possible values:

      - **bank**: Transfer to a `transfer instrument
            <https://docs.adyen.com/api-explorer/#/legalentity/latest/post/transferInstruments__resParam_id>`__ or a
            bank account."""

    BANK = "bank"
    CARD = "card"
    GRANTS = "grants"
    INTEREST = "interest"
    INTERNAL = "internal"
    ISSUED_CARD = "issuedCard"
    MIGRATION = "migration"
    PLATFORM_PAYMENT = "platformPayment"
    TOP_UP = "topUp"
    UPGRADE = "upgrade"

    __str__ = str.__str__


Category2OrStr: TypeAlias = Annotated[Category2 | str, open_enum_validator(Category2)]
