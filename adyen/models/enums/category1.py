from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Category1(str, Enum):
    """The type of transfer that results from the sweep.

    Possible values:

     - **bank**: Sweep to a `transfer instrument
            <https://docs.adyen.com/api-explorer/#/legalentity/latest/post/transferInstruments__resParam_id>`__.

    - **internal**: Transfer to another `balance account
        <https://docs.adyen.com/api-explorer/#/balanceplatform/latest/post/balanceAccounts__resParam_id>`__ within your
        platform.

    Required when setting ``priorities``."""

    BANK = "bank"
    INTERNAL = "internal"
    PLATFORM_PAYMENT = "platformPayment"

    __str__ = str.__str__


Category1OrStr: TypeAlias = Annotated[Category1 | str, open_enum_validator(Category1)]
