from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.funding_source import FundingSourceOrStr
from .enums.type14 import Type14OrStr


class CardDonations(SdkBaseModel):
    billing_sequence_number: Optional[str] = Field(default=UNSET, alias="billingSequenceNumber")
    """The sequence number for the debit. For example, send **2** if this is the second debit for the subscription. The
    sequence number is included in the notification sent to the shopper."""

    brand: Optional[str] = UNSET
    """Secondary brand of the card. For example: **plastix**, **hmclub**."""

    checkout_attempt_id: Optional[str] = Field(default=UNSET, alias="checkoutAttemptId")
    """The checkout attempt identifier."""

    cupsecureplus_smscode: Optional[str] = Field(default=UNSET, alias="cupsecureplus.smscode")
    cvc: Optional[str] = UNSET
    """The card verification code. Only collect raw card data if you are `fully PCI compliant
    <https://docs.adyen.com/development-resources/pci-dss-compliance-guide>`__."""

    encrypted_card: Optional[str] = Field(default=UNSET, alias="encryptedCard")
    """Only include this for JSON Web Encryption (JWE) implementations. The JWE-encrypted card details."""

    encrypted_card_number: Optional[str] = Field(default=UNSET, alias="encryptedCardNumber")
    """The encrypted card number."""

    encrypted_expiry_month: Optional[str] = Field(default=UNSET, alias="encryptedExpiryMonth")
    """The encrypted card expiry month."""

    encrypted_expiry_year: Optional[str] = Field(default=UNSET, alias="encryptedExpiryYear")
    """The encrypted card expiry year."""

    encrypted_password: Optional[str] = Field(default=UNSET, alias="encryptedPassword")
    """This field contains an encrypted, one-time password or an authentication code provided by the cardholder."""

    encrypted_security_code: Optional[str] = Field(default=UNSET, alias="encryptedSecurityCode")
    """The encrypted card verification code."""

    expiry_month: Optional[str] = Field(default=UNSET, alias="expiryMonth")
    """The card expiry month. Only collect raw card data if you are `fully PCI compliant
    <https://docs.adyen.com/development-resources/pci-dss-compliance-guide>`__."""

    expiry_year: Optional[str] = Field(default=UNSET, alias="expiryYear")
    """The card expiry year. Only collect raw card data if you are `fully PCI compliant
    <https://docs.adyen.com/development-resources/pci-dss-compliance-guide>`__."""

    fastlane_data: Optional[str] = Field(default=UNSET, alias="fastlaneData")
    """The encoded fastlane data blob"""

    funding_source: Optional[FundingSourceOrStr] = Field(default=UNSET, alias="fundingSource")
    """The funding source that should be used when multiple sources are available. For Brazilian combo cards, by default
    the funding source is credit. To use debit, set this value to **debit**."""

    holder_name: Optional[str] = Field(default=UNSET, alias="holderName")
    """The name of the card holder."""

    network_payment_reference: Optional[str] = Field(default=UNSET, alias="networkPaymentReference")
    """The transaction identifier from card schemes. This is the
    https://docs.adyen.com/api-explorer/Checkout/latest/post/payments#responses-200-additionalData-ResponseAdditionalDataCommon-networkTxReference
    from the response to the first payment."""

    number: Optional[str] = UNSET
    """The card number. Only collect raw card data if you are `fully PCI compliant
    <https://docs.adyen.com/development-resources/pci-dss-compliance-guide>`__."""

    recurring_detail_reference: Optional[str] = Field(default=UNSET, alias="recurringDetailReference")
    """This is the ``recurringDetailReference`` returned in the response when you created the token."""

    sdk_data: Optional[str] = Field(default=UNSET, alias="sdkData")
    """Base64-encoded JSON object containing SDK related parameters required by the SDK"""

    shopper_notification_reference: Optional[str] = Field(default=UNSET, alias="shopperNotificationReference")
    """The ``shopperNotificationReference`` returned in the response when you requested to notify the shopper. Used only
    for recurring payments in India."""

    src_correlation_id: Optional[str] = Field(default=UNSET, alias="srcCorrelationId")
    """An identifier used for the Click to Pay transaction."""

    src_digital_card_id: Optional[str] = Field(default=UNSET, alias="srcDigitalCardId")
    """The SRC reference for the Click to Pay token."""

    src_scheme: Optional[str] = Field(default=UNSET, alias="srcScheme")
    """The scheme that is being used for Click to Pay."""

    src_token_reference: Optional[str] = Field(default=UNSET, alias="srcTokenReference")
    """The reference for the Click to Pay token."""

    stored_payment_method_id: Optional[str] = Field(default=UNSET, alias="storedPaymentMethodId")
    """This is the ``recurringDetailReference`` returned in the response when you created the token."""

    three_ds2_sdk_version: Optional[str] = Field(default=UNSET, alias="threeDS2SdkVersion")
    """Required for mobile integrations. Version of the 3D Secure 2 mobile SDK."""

    type_: Optional[Type14OrStr] = Field(default=UNSET, alias="type")
    """Default payment method details. Common for scheme payment methods, and for simple payment method details."""


class CardDonationsDict(TypedDict):
    billing_sequence_number: NotRequired[str]
    brand: NotRequired[str]
    checkout_attempt_id: NotRequired[str]
    cupsecureplus_smscode: NotRequired[str]
    cvc: NotRequired[str]
    encrypted_card: NotRequired[str]
    encrypted_card_number: NotRequired[str]
    encrypted_expiry_month: NotRequired[str]
    encrypted_expiry_year: NotRequired[str]
    encrypted_password: NotRequired[str]
    encrypted_security_code: NotRequired[str]
    expiry_month: NotRequired[str]
    expiry_year: NotRequired[str]
    fastlane_data: NotRequired[str]
    funding_source: NotRequired[FundingSourceOrStr]
    holder_name: NotRequired[str]
    network_payment_reference: NotRequired[str]
    number: NotRequired[str]
    recurring_detail_reference: NotRequired[str]
    sdk_data: NotRequired[str]
    shopper_notification_reference: NotRequired[str]
    src_correlation_id: NotRequired[str]
    src_digital_card_id: NotRequired[str]
    src_scheme: NotRequired[str]
    src_token_reference: NotRequired[str]
    stored_payment_method_id: NotRequired[str]
    three_ds2_sdk_version: NotRequired[str]
    type_: NotRequired[Type14OrStr]
