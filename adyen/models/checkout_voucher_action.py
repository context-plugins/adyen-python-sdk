from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .amount14 import Amount14, Amount14Dict
from .amount15 import Amount15, Amount15Dict
from .amount16 import Amount16, Amount16Dict


class CheckoutVoucherAction(SdkBaseModel):
    alternative_reference: Optional[str] = Field(default=UNSET, alias="alternativeReference")
    """The voucher alternative reference code."""

    collection_institution_number: Optional[str] = Field(default=UNSET, alias="collectionInstitutionNumber")
    """A collection institution number (store number) for Econtext Pay-Easy ATM."""

    download_url: Optional[str] = Field(default=UNSET, alias="downloadUrl")
    """The URL to download the voucher."""

    entity: Optional[str] = UNSET
    """An entity number of Multibanco."""

    expires_at: Optional[str] = Field(default=UNSET, alias="expiresAt")
    """The date time of the voucher expiry."""

    initial_amount: Optional[Amount14] = Field(default=UNSET, alias="initialAmount")
    """The initial amount."""

    instructions_url: Optional[str] = Field(default=UNSET, alias="instructionsUrl")
    """The URL to the detailed instructions to make payment using the voucher."""

    issuer: Optional[str] = UNSET
    """The issuer of the voucher."""

    masked_telephone_number: Optional[str] = Field(default=UNSET, alias="maskedTelephoneNumber")
    """The shopper telephone number (partially masked)."""

    merchant_name: Optional[str] = Field(default=UNSET, alias="merchantName")
    """The merchant name."""

    merchant_reference: Optional[str] = Field(default=UNSET, alias="merchantReference")
    """The merchant reference."""

    pass_creation_token: Optional[str] = Field(default=UNSET, alias="passCreationToken")
    """A Base64-encoded token containing all properties of the voucher. For iOS, you can use this to pass a voucher to
    Apple Wallet."""

    payment_data: Optional[str] = Field(default=UNSET, alias="paymentData")
    """Encoded payment data."""

    payment_method_type: Optional[str] = Field(default=UNSET, alias="paymentMethodType")
    """Specifies the payment method."""

    reference: Optional[str] = UNSET
    """The voucher reference code."""

    shopper_email: Optional[str] = Field(default=UNSET, alias="shopperEmail")
    """The shopper email."""

    shopper_name: Optional[str] = Field(default=UNSET, alias="shopperName")
    """The shopper name."""

    surcharge: Optional[Amount15] = UNSET
    """The surcharge amount."""

    total_amount: Optional[Amount16] = Field(default=UNSET, alias="totalAmount")
    """The total amount (initial plus surcharge amount)."""

    type_: Literal["voucher"] = Field(default="voucher", alias="type")
    """**voucher**"""

    url: Optional[str] = UNSET
    """Specifies the URL to redirect to."""


class CheckoutVoucherActionDict(TypedDict):
    alternative_reference: NotRequired[str]
    collection_institution_number: NotRequired[str]
    download_url: NotRequired[str]
    entity: NotRequired[str]
    expires_at: NotRequired[str]
    initial_amount: NotRequired[Amount14 | Amount14Dict]
    instructions_url: NotRequired[str]
    issuer: NotRequired[str]
    masked_telephone_number: NotRequired[str]
    merchant_name: NotRequired[str]
    merchant_reference: NotRequired[str]
    pass_creation_token: NotRequired[str]
    payment_data: NotRequired[str]
    payment_method_type: NotRequired[str]
    reference: NotRequired[str]
    shopper_email: NotRequired[str]
    shopper_name: NotRequired[str]
    surcharge: NotRequired[Amount15 | Amount15Dict]
    total_amount: NotRequired[Amount16 | Amount16Dict]
    type_: NotRequired[Literal["voucher"]]
    url: NotRequired[str]
