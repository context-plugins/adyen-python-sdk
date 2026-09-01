from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, SdkBaseModel
from .enums.type74 import Type74OrStr
from .financier import Financier, FinancierDict
from .patchable_amount_dto import PatchableAmountDto, PatchableAmountDtoDict


class SourceOfFunds1(SdkBaseModel):
    adyen_processed_funds: bool = Field(alias="adyenProcessedFunds")
    """Indicates whether the funds are coming from transactions processed by Adyen. If **false**, the ``type`` is
    required."""

    amount: Optional[PatchableAmountDto] = UNSET
    """Required if ``type`` is **business**, **assetSale**, **gamblingWinnings** or **inheritance**.

    For ``type`` **business**, provide the annual turn over of the business. For ``type`` **assetSale**,
    **gamblingWinnings** or **inheritance**, provide the amount of the funds."""

    asset_months_held: Optional[int] = Field(default=UNSET, alias="assetMonthsHeld")
    """The number of months that the asset has been in possession of the user.

    For example, if the source of funds is of type **cryptocurrencyIncome** then ``assetMonthsHeld`` is the number of
    months the user has owned the cryptocurrency."""

    cryptocurrency_exchange: Optional[str] = Field(default=UNSET, alias="cryptocurrencyExchange")
    """Required if ``type`` is **cryptocurrencyIncome**. The cryptocurrency exchange where the funds were acquired."""

    date_of_funds_received: Optional[Date] = Field(default=UNSET, alias="dateOfFundsReceived")
    """Required if ``type`` is **donations** or **inheritance**. The date the funds were received, in YYYY-MM-DD
    format."""

    date_of_source_event: Optional[Date] = Field(default=UNSET, alias="dateOfSourceEvent")
    """Required if ``type`` is **assetSale** or **gamblingWinnings**. The date the funds were received, in YYYY-MM-DD
    format.

    For example, if the source of funds is of type **assetSale**, the dateOfSourceEvent is the date of the sale. If the
    source of funds is of type **gamblingWinnings**, the dateOfSourceEvent is the date of winnings."""

    description: Optional[str] = UNSET
    """Required if ``type`` is **business** or **assetSale**. A description for the source of funds.

    For example, for ``type`` **business**, provide a description of where the business transactions come from, such as
    payments through bank transfer. For ``type`` **assetSale**, provide a description of the asset. For example, the
    address of a residential property if it is a property sale."""

    financiers: Optional[list[Financier]] = UNSET
    """Required if ``type`` is **thirdPartyFunding**. Information about the financiers."""

    originator_legal_entity_id: Optional[str] = Field(default=UNSET, alias="originatorLegalEntityId")
    """Required if ``type`` is **donations** or **inheritance**. The legal entity ID representing the originator of the
    source of funds.

    For example, if the source of funds is **inheritance**, then ``originatorOfFundsReference`` should be the legal
    entity reference of the benefactor."""

    purpose: Optional[str] = UNSET
    """Required if ``type`` is **donations**. The reason for receiving the funds."""

    relationship: Optional[str] = UNSET
    """Required if ``type`` is **donations** or **inheritance**. The relationship of the originator of the funds to the
    recipient."""

    type_: Optional[Type74OrStr] = Field(default=UNSET, alias="type")
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

    website: Optional[str] = UNSET
    """Required if ``type`` is **gamblingWinnings**. The location of the gambling site for the winnings.

    For example, if the source of funds is online gambling, provide the website of the gambling company."""


class SourceOfFunds1Dict(TypedDict):
    adyen_processed_funds: bool
    amount: NotRequired[PatchableAmountDto | PatchableAmountDtoDict]
    asset_months_held: NotRequired[int]
    cryptocurrency_exchange: NotRequired[str]
    date_of_funds_received: NotRequired[Date]
    date_of_source_event: NotRequired[Date]
    description: NotRequired[str]
    financiers: NotRequired[list[Financier | FinancierDict]]
    originator_legal_entity_id: NotRequired[str]
    purpose: NotRequired[str]
    relationship: NotRequired[str]
    type_: NotRequired[Type74OrStr]
    website: NotRequired[str]
