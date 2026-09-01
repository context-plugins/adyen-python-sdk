from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, SdkBaseModel
from .enums.cancelling_entity1 import CancellingEntity1OrStr
from .enums.product_type21 import ProductType21OrStr


class NotDeliveredInfo(SdkBaseModel):
    agreed_delivery_location: Optional[str] = Field(default=UNSET, alias="agreedDeliveryLocation")
    """The delivery location specified by the cardholder. Required if **deliveredToWrongLocation** is **true**."""

    date_of_cancellation: Optional[Date] = Field(default=UNSET, alias="dateOfCancellation")
    """The date the undelivered goods or services were cancelled in YYYY-MM-DD format."""

    delivered_to_wrong_location: Optional[bool] = Field(default=UNSET, alias="deliveredToWrongLocation")
    """Indicates goods were delivered to the wrong location.

    Possible values: **true**, **false**."""

    description_of_issue: str = Field(alias="descriptionOfIssue")
    """Your description of the issue for raising a dispute of ``type`` **notDelivered**."""

    did_cardholder_return: Optional[bool] = Field(default=UNSET, alias="didCardholderReturn")
    """Indicates if the cardholder returned the goods to the merchant. Required if **isDeliveryLate** is **true**.

    Possible values: **true**, **false**."""

    is_delivery_late: Optional[bool] = Field(default=UNSET, alias="isDeliveryLate")
    """Indicates if the goods or services were delivered late. Required if **whatWasNotDelivered** is **goods**.

    Possible values: **true**, **false**."""

    is_merchant_bankrupt: Optional[bool] = Field(default=UNSET, alias="isMerchantBankrupt")
    """Indicates if the transaction was processed by a bankrupt merchant.

    Possible values: **true**, **false**."""

    is_non_fiat_or_nft: Optional[bool] = Field(default=UNSET, alias="isNonFiatOrNft")
    """Indicates if the transaction is non-fiat or non-fungible token (NFT) related.

    Possible values: **true**, **false**."""

    last_expected_date: Date = Field(alias="lastExpectedDate")
    """The date the undelivered goods or services were expected to be delivered in YYYY-MM-DD format."""

    what_was_not_delivered: ProductType21OrStr = Field(alias="whatWasNotDelivered")
    """The type of product that you expected to receive.

    Possible values: **goods**, **services**."""

    who_cancelled: Optional[CancellingEntity1OrStr] = Field(default=UNSET, alias="whoCancelled")
    """The party that initiated the cancellation of the transaction.

    Possible values: **merchant**, **cardholder**."""


class NotDeliveredInfoDict(TypedDict):
    agreed_delivery_location: NotRequired[str]
    date_of_cancellation: NotRequired[Date]
    delivered_to_wrong_location: NotRequired[bool]
    description_of_issue: str
    did_cardholder_return: NotRequired[bool]
    is_delivery_late: NotRequired[bool]
    is_merchant_bankrupt: NotRequired[bool]
    is_non_fiat_or_nft: NotRequired[bool]
    last_expected_date: Date
    what_was_not_delivered: ProductType21OrStr
    who_cancelled: NotRequired[CancellingEntity1OrStr]
