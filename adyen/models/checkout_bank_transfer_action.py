from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .amount10 import Amount10, Amount10Dict


class CheckoutBankTransferAction(SdkBaseModel):
    account_number: Optional[str] = Field(default=UNSET, alias="accountNumber")
    """The account number of the bank transfer."""

    bank_code: Optional[str] = Field(default=UNSET, alias="bankCode")
    """The bank code of the bank transfer."""

    beneficiary: Optional[str] = UNSET
    """The name of the account holder."""

    bic: Optional[str] = UNSET
    """The BIC of the IBAN."""

    branch_code: Optional[str] = Field(default=UNSET, alias="branchCode")
    """The branch code of the bank transfer."""

    download_url: Optional[str] = Field(default=UNSET, alias="downloadUrl")
    """The url to download payment details with."""

    iban: Optional[str] = UNSET
    """The IBAN of the bank transfer."""

    payment_method_type: Optional[str] = Field(default=UNSET, alias="paymentMethodType")
    """Specifies the payment method."""

    reference: Optional[str] = UNSET
    """The transfer reference."""

    routing_number: Optional[str] = Field(default=UNSET, alias="routingNumber")
    """The routing number of the bank transfer."""

    shopper_email: Optional[str] = Field(default=UNSET, alias="shopperEmail")
    """The e-mail of the shopper, included if an e-mail was sent to the shopper."""

    sort_code: Optional[str] = Field(default=UNSET, alias="sortCode")
    """The sort code of the bank transfer."""

    total_amount: Optional[Amount10] = Field(default=UNSET, alias="totalAmount")
    """The amount of the bank transfer."""

    type_: Literal["bankTransfer"] = Field(default="bankTransfer", alias="type")
    """The type of the action."""

    url: Optional[str] = UNSET
    """Specifies the URL to redirect to."""


class CheckoutBankTransferActionDict(TypedDict):
    account_number: NotRequired[str]
    bank_code: NotRequired[str]
    beneficiary: NotRequired[str]
    bic: NotRequired[str]
    branch_code: NotRequired[str]
    download_url: NotRequired[str]
    iban: NotRequired[str]
    payment_method_type: NotRequired[str]
    reference: NotRequired[str]
    routing_number: NotRequired[str]
    shopper_email: NotRequired[str]
    sort_code: NotRequired[str]
    total_amount: NotRequired[Amount10Dict]
    type_: Literal["bankTransfer"]
    url: NotRequired[str]
