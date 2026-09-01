from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class AccountType12(str, Enum):
    """Type of cardholder account used for the transaction. Allows a cardholder to select the type of account used for
    the transaction. Possible values:
    * **CardTotals**
    * **Checking**
    * **CreditCard**
    * **Default**
    * **EpurseCard**
    * **Investment**
    * **Savings**
    * **Universal**"""

    DEFAULT = "Default"
    SAVINGS = "Savings"
    CHECKING = "Checking"
    CREDIT_CARD = "CreditCard"
    UNIVERSAL = "Universal"
    INVESTMENT = "Investment"
    CARD_TOTALS = "CardTotals"
    EPURSE_CARD = "EpurseCard"

    __str__ = str.__str__


AccountType12OrStr: TypeAlias = Annotated[AccountType12 | str, open_enum_validator(AccountType12)]
