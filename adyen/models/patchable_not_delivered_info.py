from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, OptionalNullable, SdkBaseModel
from .enums.cancelling_entity import CancellingEntityOrStr
from .enums.product_type21 import ProductType21OrStr


class PatchableNotDeliveredInfo(SdkBaseModel):
    agreed_delivery_location: OptionalNullable[str] = Field(default=UNSET, alias="agreedDeliveryLocation")
    """The delivery location specified by the cardholder. Required if **deliveredToWrongLocation** is **true**."""

    date_of_cancellation: OptionalNullable[Date] = Field(default=UNSET, alias="dateOfCancellation")
    """The date the undelivered goods or services were cancelled in YYYY-MM-DD format."""

    delivered_to_wrong_location: OptionalNullable[bool] = Field(default=UNSET, alias="deliveredToWrongLocation")
    """Indicates goods were delivered to the wrong location.

    Possible values: **true**, **false**."""

    description_of_issue: Optional[str] = Field(default=UNSET, alias="descriptionOfIssue")
    """Your description of the issue for raising a dispute of ``type`` **notDelivered**."""

    did_cardholder_return: OptionalNullable[bool] = Field(default=UNSET, alias="didCardholderReturn")
    """Indicates if the cardholder returned the goods to the merchant. Required if **isDeliveryLate** is **true**.

    Possible values: **true**, **false**."""

    is_delivery_late: OptionalNullable[bool] = Field(default=UNSET, alias="isDeliveryLate")
    """Indicates if the goods or services were delivered late. Required if **whatWasNotDelivered** is **goods**.

    Possible values: **true**, **false**."""

    is_merchant_bankrupt: OptionalNullable[bool] = Field(default=UNSET, alias="isMerchantBankrupt")
    """Indicates if the transaction was processed by a bankrupt merchant.

    Possible values: **true**, **false**."""

    is_non_fiat_or_nft: OptionalNullable[bool] = Field(default=UNSET, alias="isNonFiatOrNft")
    """Indicates if the transaction is non-fiat or non-fungible token (NFT) related.

    Possible values: **true**, **false**."""

    last_expected_date: Optional[Date] = Field(default=UNSET, alias="lastExpectedDate")
    """The date the undelivered goods or services were expected to be delivered in YYYY-MM-DD format."""

    what_was_not_delivered: Optional[ProductType21OrStr] = Field(default=UNSET, alias="whatWasNotDelivered")
    """The type of product that you expected to receive.

    Possible values: **goods**, **services**."""

    who_cancelled: OptionalNullable[CancellingEntityOrStr] = Field(default=UNSET, alias="whoCancelled")
    """The party that initiated the cancellation of the transaction.

    Possible values: **merchant**, **cardholder**."""


class PatchableNotDeliveredInfoDict(TypedDict):
    agreed_delivery_location: NotRequired[str | None]
    date_of_cancellation: NotRequired[Date | None]
    delivered_to_wrong_location: NotRequired[bool | None]
    description_of_issue: NotRequired[str]
    did_cardholder_return: NotRequired[bool | None]
    is_delivery_late: NotRequired[bool | None]
    is_merchant_bankrupt: NotRequired[bool | None]
    is_non_fiat_or_nft: NotRequired[bool | None]
    last_expected_date: NotRequired[Date]
    what_was_not_delivered: NotRequired[ProductType21OrStr]
    who_cancelled: NotRequired[CancellingEntityOrStr | None]
