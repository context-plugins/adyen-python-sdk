from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .address3 import Address3, Address3Dict
from .card_details1 import CardDetails1, CardDetails1Dict
from .enums.wallet_purpose import WalletPurposeOrStr
from .name2 import Name2, Name2Dict
from .sub_merchant2 import SubMerchant2, SubMerchant2Dict


class FundRecipient(SdkBaseModel):
    iban: Optional[str] = Field(default=UNSET, alias="IBAN")
    """The IBAN of the bank account where the funds are being transferred to."""

    billing_address: Optional[Address3] = Field(default=UNSET, alias="billingAddress")
    """The address where to send the invoice."""

    payment_method: Optional[CardDetails1] = Field(default=UNSET, alias="paymentMethod")
    """The payment method used by the shopper."""

    shopper_email: Optional[str] = Field(default=UNSET, alias="shopperEmail")
    """The email address of the shopper."""

    shopper_name: Optional[Name2] = Field(default=UNSET, alias="shopperName")
    """The name of the shopper."""

    shopper_reference: Optional[str] = Field(default=UNSET, alias="shopperReference")
    """Required for recurring payments. Your reference to uniquely identify this shopper, for example user ID or account
    ID. The value is case-sensitive and must be at least three characters.
    > Your reference must not include personally identifiable information (PII) such as name or email address."""

    stored_payment_method_id: Optional[str] = Field(default=UNSET, alias="storedPaymentMethodId")
    """This is the ``recurringDetailReference`` returned in the response when you created the token."""

    sub_merchant: Optional[SubMerchant2] = Field(default=UNSET, alias="subMerchant")
    """Required for back-to-back/purchase-driven-load transactions, where the funds are taken from the shopper's stored
    card when the wallet balance is insufficient. The final merchant who will receive the money, also known as a
    `sub-merchant <https://docs.adyen.com/get-started-with-adyen/payment-glossary/#submerchant>`__."""

    telephone_number: Optional[str] = Field(default=UNSET, alias="telephoneNumber")
    """The telephone number of the shopper."""

    wallet_identifier: Optional[str] = Field(default=UNSET, alias="walletIdentifier")
    """The unique identifier for the wallet the funds are being transferred to. You can use the shopper reference or any
    other identifier."""

    wallet_owner_tax_id: Optional[str] = Field(default=UNSET, alias="walletOwnerTaxId")
    """The tax identifier of the person receiving the funds."""

    wallet_purpose: Optional[WalletPurposeOrStr] = Field(default=UNSET, alias="walletPurpose")
    """The purpose of a digital wallet transaction."""


class FundRecipientDict(TypedDict):
    iban: NotRequired[str]
    billing_address: NotRequired[Address3 | Address3Dict]
    payment_method: NotRequired[CardDetails1 | CardDetails1Dict]
    shopper_email: NotRequired[str]
    shopper_name: NotRequired[Name2 | Name2Dict]
    shopper_reference: NotRequired[str]
    stored_payment_method_id: NotRequired[str]
    sub_merchant: NotRequired[SubMerchant2 | SubMerchant2Dict]
    telephone_number: NotRequired[str]
    wallet_identifier: NotRequired[str]
    wallet_owner_tax_id: NotRequired[str]
    wallet_purpose: NotRequired[WalletPurposeOrStr]
