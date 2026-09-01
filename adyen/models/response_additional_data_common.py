from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.fraud_result_type import FraudResultTypeOrStr
from .enums.fraud_risk_level import FraudRiskLevelOrStr
from .enums.recurring_processing_model7 import RecurringProcessingModel7OrStr
from .enums.tokenization_store_operation_type import TokenizationStoreOperationTypeOrStr


class ResponseAdditionalDataCommon(SdkBaseModel):
    acquirer_account_code: Optional[str] = Field(default=UNSET, alias="acquirerAccountCode")
    """The name of the Adyen acquirer account.

    Example: PayPalSandbox_TestAcquirer

    > Only relevant for PayPal transactions."""

    acquirer_code: Optional[str] = Field(default=UNSET, alias="acquirerCode")
    """The name of the acquirer processing the payment request.

    Example: TestPmmAcquirer"""

    acquirer_reference: Optional[str] = Field(default=UNSET, alias="acquirerReference")
    """The reference number that can be used for reconciliation in case a non-Adyen acquirer is used for settlement.

    Example: 7C9N3FNBKT9"""

    alias: Optional[str] = UNSET
    """The Adyen alias of the card.

    Example: H167852639363479"""

    alias_type: Optional[str] = Field(default=UNSET, alias="aliasType")
    """The type of the card alias.

    Example: Default"""

    auth_code: Optional[str] = Field(default=UNSET, alias="authCode")
    """Authorisation code:
    * When the payment is authorised successfully, this field holds the authorisation code for the payment.
    * When the payment is not authorised, this field is empty.

    Example: 58747"""

    authorisation_mid: Optional[str] = Field(default=UNSET, alias="authorisationMid")
    """Merchant ID known by the acquirer."""

    authorised_amount_currency: Optional[str] = Field(default=UNSET, alias="authorisedAmountCurrency")
    """The currency of the authorised amount, as a three-character `ISO currency code
    <https://docs.adyen.com/development-resources/currency-codes>`__."""

    authorised_amount_value: Optional[str] = Field(default=UNSET, alias="authorisedAmountValue")
    """Value of the amount authorised.

    This amount is represented in minor units according to the `following table
    <https://docs.adyen.com/development-resources/currency-codes>`__."""

    avs_result: Optional[str] = Field(default=UNSET, alias="avsResult")
    """The AVS result code of the payment, which provides information about the outcome of the AVS check.

    For possible values, see `AVS
    <https://docs.adyen.com/risk-management/configure-standard-risk-rules/consistency-rules#billing-address-does-not-match-cardholder-address-avs>`__."""

    avs_result_raw: Optional[str] = Field(default=UNSET, alias="avsResultRaw")
    """Raw AVS result received from the acquirer, where available.

    Example: D"""

    bic: Optional[str] = UNSET
    """BIC of a bank account.

    Example: TESTNL01

    > Only relevant for SEPA Direct Debit transactions."""

    co_branded_with: Optional[str] = Field(default=UNSET, alias="coBrandedWith")
    """Includes the co-branded card information."""

    cvc_result: Optional[str] = Field(default=UNSET, alias="cvcResult")
    """The result of CVC verification."""

    cvc_result_raw: Optional[str] = Field(default=UNSET, alias="cvcResultRaw")
    """The raw result of CVC verification."""

    ds_trans_id: Optional[str] = Field(default=UNSET, alias="dsTransID")
    """Supported for 3D Secure 2. The unique transaction identifier assigned by the DS to identify a single
    transaction."""

    eci: Optional[str] = UNSET
    """The Electronic Commerce Indicator returned from the schemes for the 3DS payment session.

    Example: 02"""

    expiry_date: Optional[str] = Field(default=UNSET, alias="expiryDate")
    """The expiry date on the card.

    Example: 6/2016

    > Returned only in case of a card payment."""

    extra_costs_currency: Optional[str] = Field(default=UNSET, alias="extraCostsCurrency")
    """The currency of the extra amount charged due to additional amounts set in the skin used in the HPP payment
    request.

    Example: EUR"""

    extra_costs_value: Optional[str] = Field(default=UNSET, alias="extraCostsValue")
    """The value of the extra amount charged due to additional amounts set in the skin used in the HPP payment request.
    The amount is in minor units."""

    fraud_check_item_nr_fraud_checkname: Optional[str] = Field(
        default=UNSET, alias="fraudCheck-[itemNr]-[FraudCheckname]"
    )
    """The fraud score due to a particular fraud check. The fraud check name is found in the key of the key-value
    pair."""

    fraud_manual_review: Optional[str] = Field(default=UNSET, alias="fraudManualReview")
    """Indicates if the payment is sent to manual review."""

    fraud_result_type: Optional[FraudResultTypeOrStr] = Field(default=UNSET, alias="fraudResultType")
    """The fraud result properties of the payment. Possible values:
    * AMBER
    * GREEN
    * RED"""

    fraud_risk_level: Optional[FraudRiskLevelOrStr] = Field(default=UNSET, alias="fraudRiskLevel")
    """The risk level of the transaction as classified by the `machine learning
    <https://docs.adyen.com/risk-management/configure-your-risk-profile/machine-learning-rules/>`__ fraud risk rule. The
    risk level indicates the likelihood that a transaction will result in a fraudulent dispute. Possible values:
    * veryLow
    * low
    * medium
    * high
    * veryHigh"""

    funding_source: Optional[str] = Field(default=UNSET, alias="fundingSource")
    """Information regarding the funding type of the card. The possible return values are:
    * CHARGE
    * CREDIT
    * DEBIT
    * PREPAID
    * PREPAID_RELOADABLE

    * PREPAID_NONRELOADABLE
    * DEFFERED_DEBIT

    > This functionality requires additional configuration on Adyen's end. To enable it, contact the Support Team.

    For receiving this field in the notification, enable **Include Funding Source** in **Notifications** > **Additional
    settings**."""

    funds_availability: Optional[str] = Field(default=UNSET, alias="fundsAvailability")
    """Indicates availability of funds.

    Visa:
    * "I" (fast funds are supported)
    * "N" (otherwise)

    Mastercard:
    * "I" (product type is Prepaid or Debit, or issuing country is in CEE/HGEM list)
    * "N" (otherwise)

    > Returned when you verify a card BIN or estimate costs, and only if payoutEligible is "Y" or "D"."""

    inferred_refusal_reason: Optional[str] = Field(default=UNSET, alias="inferredRefusalReason")
    """Provides the more granular indication of why a transaction was refused. When a transaction fails with either
    "Refused", "Restricted Card", "Transaction Not Permitted", "Not supported" or "DeclinedNon Generic" refusalReason
    from the issuer, Adyen cross references its PSP-wide data for extra insight into the refusal reason. If an inferred
    refusal reason is available, the ``inferredRefusalReason``, field is populated and the ``refusalReason``, is set to
    "Not Supported".

    Possible values:

    * 3D Secure Mandated
    * Closed Account
    * ContAuth Not Supported
    * CVC Mandated
    * Ecommerce Not Allowed
    * Crossborder Not Supported
    * Card Updated

    * Low Authrate Bin
    * Non-reloadable prepaid card"""

    is_card_commercial: Optional[str] = Field(default=UNSET, alias="isCardCommercial")
    """Indicates if the card is used for business purposes only."""

    issuer_country: Optional[str] = Field(default=UNSET, alias="issuerCountry")
    """The issuing country of the card based on the BIN list that Adyen maintains.

    Example: JP"""

    liability_shift: Optional[str] = Field(default=UNSET, alias="liabilityShift")
    """A Boolean value indicating whether a liability shift was offered for this payment."""

    mc_bank_net_reference_number: Optional[str] = Field(default=UNSET, alias="mcBankNetReferenceNumber")
    """The ``mcBankNetReferenceNumber``, is a minimum of six characters and a maximum of nine characters long.

    > Contact Support Team to enable this field."""

    merchant_advice_code: Optional[str] = Field(default=UNSET, alias="merchantAdviceCode")
    """The Merchant Advice Code (MAC) can be returned by Mastercard issuers for refused payments. If present, the MAC
    contains information about why the payment failed, and whether it can be retried.

    For more information see `Mastercard Merchant Advice Codes
    <https://docs.adyen.com/development-resources/raw-acquirer-responses#mastercard-merchant-advice-codes>`__."""

    merchant_reference: Optional[str] = Field(default=UNSET, alias="merchantReference")
    """The reference provided for the transaction."""

    network_processing_mode: Optional[str] = Field(default=UNSET, alias="networkProcessingMode")
    """Indicates the processing flow.

    Possible values:
    * **sale**: You do not need to separately capture the funds, because capture happens automatically as part of the
        transaction.
    * **auth**: If you have not `configured automatic capture for the transaction
        <https://docs.adyen.com/online-payments/capture#types-of-capture>`__, you must manually capture the funds."""

    network_tx_reference: Optional[str] = Field(default=UNSET, alias="networkTxReference")
    """Returned in the response if you are not tokenizing with Adyen and are using the Merchant-initiated transactions
    (MIT) framework from Mastercard or Visa.

    This contains either the Mastercard Trace ID or the Visa Transaction ID."""

    owner_name: Optional[str] = Field(default=UNSET, alias="ownerName")
    """The owner name of a bank account.

    Only relevant for SEPA Direct Debit transactions."""

    payment_account_reference: Optional[str] = Field(default=UNSET, alias="paymentAccountReference")
    """The Payment Account Reference (PAR) value links a network token with the underlying primary account number (PAN).
    The PAR value consists of 29 uppercase alphanumeric characters."""

    payment_method: Optional[str] = Field(default=UNSET, alias="paymentMethod")
    """The payment method used in the transaction."""

    payment_method_variant: Optional[str] = Field(default=UNSET, alias="paymentMethodVariant")
    """The Adyen sub-variant of the payment method used for the payment request.

    For more information, refer to `PaymentMethodVariant
    <https://docs.adyen.com/development-resources/paymentmethodvariant>`__.

    Example: mcpro"""

    payout_eligible: Optional[str] = Field(default=UNSET, alias="payoutEligible")
    """Indicates whether a payout is eligible or not for this card.

    Visa:
    * "Y"
    * "N"

    Mastercard:
    * "Y" (domestic and cross-border)

    * "D" (only domestic)
    * "N" (no MoneySend)
    * "U" (unknown)"""

    realtime_account_updater_status: Optional[str] = Field(default=UNSET, alias="realtimeAccountUpdaterStatus")
    """The response code from the Real Time Account Updater service.

    Possible return values are:
    * CardChanged
    * CardExpiryChanged
    * CloseAccount

    * ContactCardAccountHolder"""

    receipt_free_text: Optional[str] = Field(default=UNSET, alias="receiptFreeText")
    """Message to be displayed on the terminal."""

    recurring_contract_types: Optional[str] = Field(default=UNSET, alias="recurring.contractTypes")
    """The recurring contract types applicable to the transaction."""

    recurring_first_psp_reference: Optional[str] = Field(default=UNSET, alias="recurring.firstPspReference")
    """The ``pspReference``, of the first recurring payment that created the recurring detail.

    This functionality requires additional configuration on Adyen's end. To enable it, contact the Support Team."""

    recurring_recurring_detail_reference: Optional[str] = Field(
        default=UNSET, alias="recurring.recurringDetailReference"
    )
    """The reference that uniquely identifies the recurring transaction."""

    recurring_shopper_reference: Optional[str] = Field(default=UNSET, alias="recurring.shopperReference")
    """The provided reference of the shopper for a recurring transaction."""

    recurring_processing_model: Optional[RecurringProcessingModel7OrStr] = Field(
        default=UNSET, alias="recurringProcessingModel"
    )
    """The processing model used for the recurring transaction."""

    referred: Optional[str] = UNSET
    """If the payment is referred, this field is set to true.

    This field is unavailable if the payment is referred and is usually not returned with ecommerce transactions.

    Example: true"""

    refusal_reason_raw: Optional[str] = Field(default=UNSET, alias="refusalReasonRaw")
    """Raw refusal reason received from the acquirer, where available.

    Example: AUTHORISED"""

    request_amount: Optional[str] = Field(default=UNSET, alias="requestAmount")
    """The amount of the payment request."""

    request_currency_code: Optional[str] = Field(default=UNSET, alias="requestCurrencyCode")
    """The currency of the payment request."""

    shopper_interaction: Optional[str] = Field(default=UNSET, alias="shopperInteraction")
    """The shopper interaction type of the payment request.

    Example: Ecommerce"""

    shopper_reference: Optional[str] = Field(default=UNSET, alias="shopperReference")
    """The shopperReference passed in the payment request.

    Example: AdyenTestShopperXX"""

    terminal_id: Optional[str] = Field(default=UNSET, alias="terminalId")
    """The terminal ID used in a point-of-sale payment.

    Example: 06022622"""

    three_d_authenticated: Optional[str] = Field(default=UNSET, alias="threeDAuthenticated")
    """A Boolean value indicating whether 3DS authentication was completed on this payment.

    Example: true"""

    three_d_authenticated_response: Optional[str] = Field(default=UNSET, alias="threeDAuthenticatedResponse")
    """The raw 3DS authentication result from the card issuer.

    Example: N"""

    three_d_offered: Optional[str] = Field(default=UNSET, alias="threeDOffered")
    """A Boolean value indicating whether 3DS was offered for this payment.

    Example: true"""

    three_d_offered_response: Optional[str] = Field(default=UNSET, alias="threeDOfferedResponse")
    """The raw enrollment result from the 3DS directory services of the card schemes.

    Example: Y"""

    three_ds_version: Optional[str] = Field(default=UNSET, alias="threeDSVersion")
    """The 3D Secure 2 version."""

    tokenization_shopper_reference: Optional[str] = Field(default=UNSET, alias="tokenization.shopperReference")
    """The reference for the shopper that you sent when tokenizing the payment details."""

    tokenization_store_operation_type: Optional[TokenizationStoreOperationTypeOrStr] = Field(
        default=UNSET, alias="tokenization.store.operationType"
    )
    """The operation performed on the token. Possible values:

    * **created**: the token has been created.
    * **updated**: the existing token has been updated.
    * **alreadyExisting**: the details have already been stored."""

    tokenization_stored_payment_method_id: Optional[str] = Field(
        default=UNSET, alias="tokenization.storedPaymentMethodId"
    )
    """The reference that uniquely identifies tokenized payment details."""

    transaction_link_id: Optional[str] = Field(default=UNSET, alias="transactionLinkId")
    """Returned in the response for Mastercard payments.

    This contains the Mastercard Transaction Link Identifier (TLID)."""

    visa_transaction_id: Optional[str] = Field(default=UNSET, alias="visaTransactionId")
    """The ``visaTransactionId``, has a fixed length of 15 numeric characters.

    > Contact Support Team to enable this field."""

    xid: Optional[str] = UNSET
    """The 3DS transaction ID of the 3DS session sent in notifications. The value is Base64-encoded and is returned for
    transactions with directoryResponse 'N' or 'Y'.

    Example: ODgxNDc2MDg2MDExODk5MAAAAAA="""


class ResponseAdditionalDataCommonDict(TypedDict):
    acquirer_account_code: NotRequired[str]
    acquirer_code: NotRequired[str]
    acquirer_reference: NotRequired[str]
    alias: NotRequired[str]
    alias_type: NotRequired[str]
    auth_code: NotRequired[str]
    authorisation_mid: NotRequired[str]
    authorised_amount_currency: NotRequired[str]
    authorised_amount_value: NotRequired[str]
    avs_result: NotRequired[str]
    avs_result_raw: NotRequired[str]
    bic: NotRequired[str]
    co_branded_with: NotRequired[str]
    cvc_result: NotRequired[str]
    cvc_result_raw: NotRequired[str]
    ds_trans_id: NotRequired[str]
    eci: NotRequired[str]
    expiry_date: NotRequired[str]
    extra_costs_currency: NotRequired[str]
    extra_costs_value: NotRequired[str]
    fraud_check_item_nr_fraud_checkname: NotRequired[str]
    fraud_manual_review: NotRequired[str]
    fraud_result_type: NotRequired[FraudResultTypeOrStr]
    fraud_risk_level: NotRequired[FraudRiskLevelOrStr]
    funding_source: NotRequired[str]
    funds_availability: NotRequired[str]
    inferred_refusal_reason: NotRequired[str]
    is_card_commercial: NotRequired[str]
    issuer_country: NotRequired[str]
    liability_shift: NotRequired[str]
    mc_bank_net_reference_number: NotRequired[str]
    merchant_advice_code: NotRequired[str]
    merchant_reference: NotRequired[str]
    network_processing_mode: NotRequired[str]
    network_tx_reference: NotRequired[str]
    owner_name: NotRequired[str]
    payment_account_reference: NotRequired[str]
    payment_method: NotRequired[str]
    payment_method_variant: NotRequired[str]
    payout_eligible: NotRequired[str]
    realtime_account_updater_status: NotRequired[str]
    receipt_free_text: NotRequired[str]
    recurring_contract_types: NotRequired[str]
    recurring_first_psp_reference: NotRequired[str]
    recurring_recurring_detail_reference: NotRequired[str]
    recurring_shopper_reference: NotRequired[str]
    recurring_processing_model: NotRequired[RecurringProcessingModel7OrStr]
    referred: NotRequired[str]
    refusal_reason_raw: NotRequired[str]
    request_amount: NotRequired[str]
    request_currency_code: NotRequired[str]
    shopper_interaction: NotRequired[str]
    shopper_reference: NotRequired[str]
    terminal_id: NotRequired[str]
    three_d_authenticated: NotRequired[str]
    three_d_authenticated_response: NotRequired[str]
    three_d_offered: NotRequired[str]
    three_d_offered_response: NotRequired[str]
    three_ds_version: NotRequired[str]
    tokenization_shopper_reference: NotRequired[str]
    tokenization_store_operation_type: NotRequired[TokenizationStoreOperationTypeOrStr]
    tokenization_stored_payment_method_id: NotRequired[str]
    transaction_link_id: NotRequired[str]
    visa_transaction_id: NotRequired[str]
    xid: NotRequired[str]
