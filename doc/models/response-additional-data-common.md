
# Response Additional Data Common

*This model accepts additional fields of type Any.*

## Structure

`ResponseAdditionalDataCommon`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `acquirer_account_code` | `str` | Optional | The name of the Adyen acquirer account.<br><br>Example: PayPalSandbox_TestAcquirer<br><br>> Only relevant for PayPal transactions. |
| `acquirer_code` | `str` | Optional | The name of the acquirer processing the payment request.<br><br>Example: TestPmmAcquirer |
| `acquirer_reference` | `str` | Optional | The reference number that can be used for reconciliation in case a non-Adyen acquirer is used for settlement.<br><br>Example: 7C9N3FNBKT9 |
| `alias` | `str` | Optional | The Adyen alias of the card.<br><br>Example: H167852639363479 |
| `alias_type` | `str` | Optional | The type of the card alias.<br><br>Example: Default |
| `auth_code` | `str` | Optional | Authorisation code:<br><br>* When the payment is authorised successfully, this field holds the authorisation code for the payment.<br>* When the payment is not authorised, this field is empty.<br><br>Example: 58747 |
| `authorisation_mid` | `str` | Optional | Merchant ID known by the acquirer. |
| `authorised_amount_currency` | `str` | Optional | The currency of the authorised amount, as a three-character [ISO currency code](https://docs.adyen.com/development-resources/currency-codes). |
| `authorised_amount_value` | `str` | Optional | Value of the amount authorised.<br><br>This amount is represented in minor units according to the [following table](https://docs.adyen.com/development-resources/currency-codes). |
| `avs_result` | `str` | Optional | The AVS result code of the payment, which provides information about the outcome of the AVS check.<br><br>For possible values, see [AVS](https://docs.adyen.com/risk-management/configure-standard-risk-rules/consistency-rules#billing-address-does-not-match-cardholder-address-avs). |
| `avs_result_raw` | `str` | Optional | Raw AVS result received from the acquirer, where available.<br><br>Example: D |
| `bic` | `str` | Optional | BIC of a bank account.<br><br>Example: TESTNL01<br><br>> Only relevant for SEPA Direct Debit transactions. |
| `co_branded_with` | `str` | Optional | Includes the co-branded card information. |
| `cvc_result` | `str` | Optional | The result of CVC verification. |
| `cvc_result_raw` | `str` | Optional | The raw result of CVC verification. |
| `ds_trans_id` | `str` | Optional | Supported for 3D Secure 2. The unique transaction identifier assigned by the DS to identify a single transaction. |
| `eci` | `str` | Optional | The Electronic Commerce Indicator returned from the schemes for the 3DS payment session.<br><br>Example: 02 |
| `expiry_date` | `str` | Optional | The expiry date on the card.<br><br>Example: 6/2016<br><br>> Returned only in case of a card payment. |
| `extra_costs_currency` | `str` | Optional | The currency of the extra amount charged due to additional amounts set in the skin used in the HPP payment request.<br><br>Example: EUR |
| `extra_costs_value` | `str` | Optional | The value of the extra amount charged due to additional amounts set in the skin used in the HPP payment request. The amount is in minor units. |
| `fraud_check_item_nr_fraud_checkname` | `str` | Optional | The fraud score due to a particular fraud check. The fraud check name is found in the key of the key-value pair. |
| `fraud_manual_review` | `str` | Optional | Indicates if the payment is sent to manual review. |
| `fraud_result_type` | [`FraudResultType`](../../doc/models/fraud-result-type.md) | Optional | - |
| `fraud_risk_level` | [`FraudRiskLevel`](../../doc/models/fraud-risk-level.md) | Optional | - |
| `funding_source` | `str` | Optional | Information regarding the funding type of the card. The possible return values are:<br><br>* CHARGE<br><br>* CREDIT<br><br>* DEBIT<br><br>* PREPAID<br><br>* PREPAID_RELOADABLE<br><br>* PREPAID_NONRELOADABLE<br><br>* DEFFERED_DEBIT<br><br>> This functionality requires additional configuration on Adyen's end. To enable it, contact the Support Team.<br><br>For receiving this field in the notification, enable **Include Funding Source** in **Notifications** > **Additional settings**. |
| `funds_availability` | `str` | Optional | Indicates availability of funds.<br><br>Visa:<br><br>* "I" (fast funds are supported)<br>* "N" (otherwise)<br><br>Mastercard:<br><br>* "I" (product type is Prepaid or Debit, or issuing country is in CEE/HGEM list)<br>* "N" (otherwise)<br><br>> Returned when you verify a card BIN or estimate costs, and only if payoutEligible is "Y" or "D". |
| `inferred_refusal_reason` | `str` | Optional | Provides the more granular indication of why a transaction was refused. When a transaction fails with either "Refused", "Restricted Card", "Transaction Not Permitted", "Not supported" or "DeclinedNon Generic" refusalReason from the issuer, Adyen cross references its PSP-wide data for extra insight into the refusal reason. If an inferred refusal reason is available, the `inferredRefusalReason`, field is populated and the `refusalReason`, is set to "Not Supported".<br><br>Possible values:<br><br>* 3D Secure Mandated<br><br>* Closed Account<br><br>* ContAuth Not Supported<br><br>* CVC Mandated<br><br>* Ecommerce Not Allowed<br><br>* Crossborder Not Supported<br><br>* Card Updated<br><br>* Low Authrate Bin<br><br>* Non-reloadable prepaid card |
| `is_card_commercial` | `str` | Optional | Indicates if the card is used for business purposes only. |
| `issuer_country` | `str` | Optional | The issuing country of the card based on the BIN list that Adyen maintains.<br><br>Example: JP |
| `liability_shift` | `str` | Optional | A Boolean value indicating whether a liability shift was offered for this payment. |
| `mc_bank_net_reference_number` | `str` | Optional | The `mcBankNetReferenceNumber`, is a minimum of six characters and a maximum of nine characters long.<br><br>> Contact Support Team to enable this field. |
| `merchant_advice_code` | `str` | Optional | The Merchant Advice Code (MAC) can be returned by Mastercard issuers for refused payments. If present, the MAC contains information about why the payment failed, and whether it can be retried.<br><br>For more information see [Mastercard Merchant Advice Codes](https://docs.adyen.com/development-resources/raw-acquirer-responses#mastercard-merchant-advice-codes). |
| `merchant_reference` | `str` | Optional | The reference provided for the transaction. |
| `network_processing_mode` | `str` | Optional | Indicates the processing flow.<br><br>Possible values:<br><br>* **sale**: You do not need to separately capture the funds, because capture happens automatically as part of the transaction.<br>* **auth**: If you have not [configured automatic capture for the transaction](https://docs.adyen.com/online-payments/capture#types-of-capture), you must manually capture the funds. |
| `network_tx_reference` | `str` | Optional | Returned in the response if you are not tokenizing with Adyen and are using the Merchant-initiated transactions (MIT) framework from Mastercard or Visa.<br><br>This contains either the Mastercard Trace ID or the Visa Transaction ID. |
| `owner_name` | `str` | Optional | The owner name of a bank account.<br><br>Only relevant for SEPA Direct Debit transactions. |
| `payment_account_reference` | `str` | Optional | The Payment Account Reference (PAR) value links a network token with the underlying primary account number (PAN). The PAR value consists of 29 uppercase alphanumeric characters. |
| `payment_method` | `str` | Optional | The payment method used in the transaction. |
| `payment_method_variant` | `str` | Optional | The Adyen sub-variant of the payment method used for the payment request.<br><br>For more information, refer to [PaymentMethodVariant](https://docs.adyen.com/development-resources/paymentmethodvariant).<br><br>Example: mcpro |
| `payout_eligible` | `str` | Optional | Indicates whether a payout is eligible or not for this card.<br><br>Visa:<br><br>* "Y"<br>* "N"<br><br>Mastercard:<br><br>* "Y" (domestic and cross-border)<br><br>* "D" (only domestic)<br><br>* "N" (no MoneySend)<br><br>* "U" (unknown) |
| `realtime_account_updater_status` | `str` | Optional | The response code from the Real Time Account Updater service.<br><br>Possible return values are:<br><br>* CardChanged<br><br>* CardExpiryChanged<br><br>* CloseAccount<br><br>* ContactCardAccountHolder |
| `receipt_free_text` | `str` | Optional | Message to be displayed on the terminal. |
| `recurring_contract_types` | `str` | Optional | The recurring contract types applicable to the transaction. |
| `recurring_first_psp_reference` | `str` | Optional | The `pspReference`, of the first recurring payment that created the recurring detail.<br><br>This functionality requires additional configuration on Adyen's end. To enable it, contact the Support Team. |
| `recurring_recurring_detail_reference` | `str` | Optional | The reference that uniquely identifies the recurring transaction. |
| `recurring_shopper_reference` | `str` | Optional | The provided reference of the shopper for a recurring transaction. |
| `recurring_processing_model` | [`RecurringProcessingModel7`](../../doc/models/recurring-processing-model-7.md) | Optional | - |
| `referred` | `str` | Optional | If the payment is referred, this field is set to true.<br><br>This field is unavailable if the payment is referred and is usually not returned with ecommerce transactions.<br><br>Example: true |
| `refusal_reason_raw` | `str` | Optional | Raw refusal reason received from the acquirer, where available.<br><br>Example: AUTHORISED |
| `request_amount` | `str` | Optional | The amount of the payment request. |
| `request_currency_code` | `str` | Optional | The currency of the payment request. |
| `shopper_interaction` | `str` | Optional | The shopper interaction type of the payment request.<br><br>Example: Ecommerce |
| `shopper_reference` | `str` | Optional | The shopperReference passed in the payment request.<br><br>Example: AdyenTestShopperXX |
| `terminal_id` | `str` | Optional | The terminal ID used in a point-of-sale payment.<br><br>Example: 06022622 |
| `three_d_authenticated` | `str` | Optional | A Boolean value indicating whether 3DS authentication was completed on this payment.<br><br>Example: true |
| `three_d_authenticated_response` | `str` | Optional | The raw 3DS authentication result from the card issuer.<br><br>Example: N |
| `three_d_offered` | `str` | Optional | A Boolean value indicating whether 3DS was offered for this payment.<br><br>Example: true |
| `three_d_offered_response` | `str` | Optional | The raw enrollment result from the 3DS directory services of the card schemes.<br><br>Example: Y |
| `three_ds_version` | `str` | Optional | The 3D Secure 2 version. |
| `tokenization_shopper_reference` | `str` | Optional | The reference for the shopper that you sent when tokenizing the payment details. |
| `tokenization_store_operation_type` | [`TokenizationStoreOperationType`](../../doc/models/tokenization-store-operation-type.md) | Optional | - |
| `tokenization_stored_payment_method_id` | `str` | Optional | The reference that uniquely identifies tokenized payment details. |
| `transaction_link_id` | `str` | Optional | Returned in the response for Mastercard payments.<br><br>This contains the Mastercard Transaction Link Identifier (TLID). |
| `visa_transaction_id` | `str` | Optional | The `visaTransactionId`, has a fixed length of 15 numeric characters.<br><br>> Contact Support Team to enable this field. |
| `xid` | `str` | Optional | The 3DS transaction ID of the 3DS session sent in notifications. The value is Base64-encoded and is returned for transactions with directoryResponse 'N' or 'Y'.<br><br>Example: ODgxNDc2MDg2MDExODk5MAAAAAA= |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.response_additional_data_common import ResponseAdditionalDataCommon

response_additional_data_common = ResponseAdditionalDataCommon(
    acquirer_account_code='acquirerAccountCode0',
    acquirer_code='acquirerCode6',
    acquirer_reference='acquirerReference2',
    alias='alias4',
    alias_type='aliasType6',
    cvc_result='1 Matches',
    cvc_result_raw='M',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

