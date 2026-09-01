from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type74(str, Enum):
    """The type of the source of funds.



    Possible values:
    * **business**
    * **employment**
    * **donations**
    * **inheritance**
    * **financialAid**
    * **rentalIncome**
    * **dividendIncome**
    * **royaltyIncome**
    * **thirdPartyFunding**
    * **pensionIncome**
    * **insuranceSettlement**
    * **cryptocurrencyIncome**
    * **assetSale**
    * **loans**
    * **gamblingWinnings**"""

    BUSINESS = "business"
    EMPLOYMENT = "employment"
    DONATIONS = "donations"
    INHERITANCE = "inheritance"
    FINANCIAL_AID = "financialAid"
    RENTAL_INCOME = "rentalIncome"
    DIVIDEND_INCOME = "dividendIncome"
    ROYALTY_INCOME = "royaltyIncome"
    THIRD_PARTY_FUNDING = "thirdPartyFunding"
    PENSION_INCOME = "pensionIncome"
    INSURANCE_SETTLEMENT = "insuranceSettlement"
    CRYPTOCURRENCY_INCOME = "cryptocurrencyIncome"
    ASSET_SALE = "assetSale"
    LOANS = "loans"
    GAMBLING_WINNINGS = "gamblingWinnings"

    __str__ = str.__str__


Type74OrStr: TypeAlias = Annotated[Type74 | str, open_enum_validator(Type74)]
