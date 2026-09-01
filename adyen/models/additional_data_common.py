from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.industry_usage import IndustryUsageOrStr


class AdditionalDataCommon(SdkBaseModel):
    requested_test_acquirer_response_code: Optional[str] = Field(
        default=UNSET, alias="RequestedTestAcquirerResponseCode"
    )
    """Triggers test scenarios that allow to replicate certain acquirer response codes. See `Testing result codes and
    refusal reasons <https://docs.adyen.com/development-resources/testing/result-codes/>`__ to learn about the possible
    values, and the ``refusalReason`` values you can trigger."""

    requested_test_error_response_code: Optional[str] = Field(default=UNSET, alias="RequestedTestErrorResponseCode")
    """Triggers test scenarios that allow to replicate certain communication errors.

    Allowed values:
    * **NO_CONNECTION_AVAILABLE** – There wasn't a connection available to service the outgoing communication.
    This is a transient, retriable error since no messaging could be initiated to an issuing system (or third-party
    acquiring system). Therefore, the header Transient-Error: true is returned in the response. A subsequent request
    using the same idempotency key will be processed as if it was the first request.
    * **IOEXCEPTION_RECEIVED** – Something went wrong during transmission of the message or receiving the response.
    This is a classified as non-transient because the message could have been received by the issuing party and been
    acted upon. No transient error header is returned. If using idempotency, the (error) response is stored as the final
    result for the idempotency key. Subsequent messages with the same idempotency key not be processed beyond returning
    the stored response."""

    allow_partial_auth: Optional[str] = Field(default=UNSET, alias="allowPartialAuth")
    """Set to true to authorise a part of the requested amount in case the cardholder does not have enough funds on
    their account. If a payment was partially authorised, the response includes resultCode: PartiallyAuthorised and the
    authorised amount in additionalData.authorisedAmountValue. To enable this functionality, contact our Support
    Team."""

    authorisation_type: Optional[str] = Field(default=UNSET, alias="authorisationType")
    """Flags a card payment request for either pre-authorisation or final authorisation. For more information, refer to
    `Authorisation types <https://docs.adyen.com/online-payments/adjust-authorisation#authorisation-types>`__.

    Allowed values:
    * **PreAuth** – flags the payment request to be handled as a pre-authorisation.
    * **FinalAuth** – flags the payment request to be handled as a final authorisation."""

    auto_rescue: Optional[str] = Field(default=UNSET, alias="autoRescue")
    """Set to **true** to enable `Auto Rescue <https://docs.adyen.com/online-payments/auto-rescue/>`__ for a
    transaction. Use the ``maxDaysToRescue`` to specify a rescue window."""

    custom_routing_flag: Optional[str] = Field(default=UNSET, alias="customRoutingFlag")
    """Allows you to determine or override the acquirer account that should be used for the transaction.

    If you need to process a payment with an acquirer different from a default one, you can set up a corresponding
    configuration on the Adyen payments platform. Then you can pass a custom routing flag in a payment request's
    additional data to target a specific acquirer.

    To enable this functionality, contact `Support <https://www.adyen.help/hc/en-us/requests/new>`__."""

    industry_usage: Optional[IndustryUsageOrStr] = Field(default=UNSET, alias="industryUsage")
    """In case of `asynchronous authorisation adjustment
    <https://docs.adyen.com/online-payments/adjust-authorisation#adjust-authorisation>`__, this field denotes why the
    additional payment is made.

    Possible values:

     * **NoShow**: An incremental charge is carried out because of a no-show for a guaranteed reservation.

     * **DelayedCharge**: An incremental charge is carried out to process an additional payment after the original
            services have been rendered and the respective payment has been processed."""

    manual_capture: Optional[str] = Field(default=UNSET, alias="manualCapture")
    """Set to **true** to require `manual capture <https://docs.adyen.com/online-payments/capture>`__ for the
    transaction."""

    max_days_to_rescue: Optional[str] = Field(default=UNSET, alias="maxDaysToRescue")
    """The rescue window for a transaction, in days, when ``autoRescue`` is set to **true**. You can specify a value
    between 1 and 48.

    * For `cards <https://docs.adyen.com/online-payments/auto-rescue/cards/>`__, the default is one calendar month.
     * For `SEPA <https://docs.adyen.com/online-payments/auto-rescue/sepa/>`__, the default is 42 days."""

    network_tx_reference: Optional[str] = Field(default=UNSET, alias="networkTxReference")
    """Allows you to link the transaction to the original or previous one in a subscription/card-on-file chain. This
    field is required for token-based transactions where Adyen does not tokenize the card.

    Transaction identifier from card schemes, for example, Mastercard Trace ID or the Visa Transaction ID.

    Submit the original transaction ID of the contract in your payment request if you are not tokenizing card details
    with Adyen and are making a merchant-initiated transaction (MIT) for subsequent charges.

    Make sure you are sending ``shopperInteraction`` **ContAuth** and ``recurringProcessingModel`` **Subscription** or
    **UnscheduledCardOnFile** to ensure that the transaction is classified as MIT."""

    overwrite_brand: Optional[str] = Field(default=UNSET, alias="overwriteBrand")
    """Boolean indicator that can be optionally used for performing debit transactions on combo cards (for example,
    combo cards in Brazil). This is not mandatory but we recommend that you set this to true if you want to use the
    ``selectedBrand`` value to specify how to process the transaction."""

    sub_merchant_city: Optional[str] = Field(default=UNSET, alias="subMerchantCity")
    """This field is required if the transaction is performed by a registered payment facilitator. This field must
    contain the city of the actual merchant's address.
    * Format: alpha-numeric.
    * Maximum length: 13 characters."""

    sub_merchant_country: Optional[str] = Field(default=UNSET, alias="subMerchantCountry")
    """This field is required if the transaction is performed by a registered payment facilitator. This field must
    contain the three-letter country code of the actual merchant's address.
    * Format: alpha-numeric.
    * Fixed length: 3 characters."""

    sub_merchant_email: Optional[str] = Field(default=UNSET, alias="subMerchantEmail")
    """This field is required for transactions performed by registered payment facilitators. This field contains the
    email address of the sub-merchant.
    * Format: Alphanumeric
    * Maximum length: 40 characters"""

    sub_merchant_id: Optional[str] = Field(default=UNSET, alias="subMerchantID")
    """This field contains an identifier of the actual merchant when a transaction is submitted via a payment
    facilitator. The payment facilitator must send in this unique ID.

    A unique identifier per submerchant that is required if the transaction is performed by a registered payment
    facilitator.
    * Format: alpha-numeric.
    * Fixed length: 15 characters."""

    sub_merchant_name: Optional[str] = Field(default=UNSET, alias="subMerchantName")
    """This field is required if the transaction is performed by a registered payment facilitator. This field must
    contain the name of the actual merchant.
    * Format: alpha-numeric.
    * Maximum length: 22 characters."""

    sub_merchant_phone_number: Optional[str] = Field(default=UNSET, alias="subMerchantPhoneNumber")
    """This field is required for transactions performed by registered payment facilitators. This field contains the
    phone number of the sub-merchant.* Format: Alphanumeric
    * Maximum length: 20 characters"""

    sub_merchant_postal_code: Optional[str] = Field(default=UNSET, alias="subMerchantPostalCode")
    """This field is required if the transaction is performed by a registered payment facilitator. This field must
    contain the postal code of the actual merchant's address.
    * Format: alpha-numeric.
    * Maximum length: 10 characters."""

    sub_merchant_state: Optional[str] = Field(default=UNSET, alias="subMerchantState")
    """This field is required if the transaction is performed by a registered payment facilitator, and if applicable to
    the country. This field must contain the state code of the actual merchant's address.
    * Format: alpha-numeric.
    * Maximum length: 3 characters."""

    sub_merchant_street: Optional[str] = Field(default=UNSET, alias="subMerchantStreet")
    """This field is required if the transaction is performed by a registered payment facilitator. This field must
    contain the street of the actual merchant's address.
    * Format: alpha-numeric.
    * Maximum length: 60 characters."""

    sub_merchant_tax_id: Optional[str] = Field(default=UNSET, alias="subMerchantTaxId")
    """This field is required if the transaction is performed by a registered payment facilitator. This field must
    contain the tax ID of the actual merchant.
    * Format: alpha-numeric.
    * Fixed length: 11 or 14 characters."""

    transaction_link_id: Optional[str] = Field(default=UNSET, alias="transactionLinkId")
    """Allows you to link the transaction to the original or previous one in a subscription/card-on-file chain For
    Mastercard payments. This field is required for token-based transactions where Adyen does not tokenize the card.

    Transaction identifier from Mastercard.

    Submit the original transaction ID of the contract in your payment request if you are not tokenizing card details
    with Adyen and are making a merchant-initiated transaction (MIT) for subsequent charges.

    Make sure you are sending ``shopperInteraction`` **ContAuth** and ``recurringProcessingModel`` **Subscription** or
    **UnscheduledCardOnFile** to ensure that the transaction is classified as MIT."""


class AdditionalDataCommonDict(TypedDict):
    requested_test_acquirer_response_code: NotRequired[str]
    requested_test_error_response_code: NotRequired[str]
    allow_partial_auth: NotRequired[str]
    authorisation_type: NotRequired[str]
    auto_rescue: NotRequired[str]
    custom_routing_flag: NotRequired[str]
    industry_usage: NotRequired[IndustryUsageOrStr]
    manual_capture: NotRequired[str]
    max_days_to_rescue: NotRequired[str]
    network_tx_reference: NotRequired[str]
    overwrite_brand: NotRequired[str]
    sub_merchant_city: NotRequired[str]
    sub_merchant_country: NotRequired[str]
    sub_merchant_email: NotRequired[str]
    sub_merchant_id: NotRequired[str]
    sub_merchant_name: NotRequired[str]
    sub_merchant_phone_number: NotRequired[str]
    sub_merchant_postal_code: NotRequired[str]
    sub_merchant_state: NotRequired[str]
    sub_merchant_street: NotRequired[str]
    sub_merchant_tax_id: NotRequired[str]
    transaction_link_id: NotRequired[str]
