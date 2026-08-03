
# Card Donations

*This model accepts additional fields of type Any.*

## Structure

`CardDonations`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `billing_sequence_number` | `str` | Optional | The sequence number for the debit. For example, send **2** if this is the second debit for the subscription. The sequence number is included in the notification sent to the shopper. |
| `brand` | `str` | Optional | Secondary brand of the card. For example: **plastix**, **hmclub**. |
| `checkout_attempt_id` | `str` | Optional | The checkout attempt identifier. |
| `cupsecureplus_smscode` | `str` | Optional | - |
| `cvc` | `str` | Optional | The card verification code. Only collect raw card data if you are [fully PCI compliant](https://docs.adyen.com/development-resources/pci-dss-compliance-guide). |
| `encrypted_card` | `str` | Optional | Only include this for JSON Web Encryption (JWE) implementations. The JWE-encrypted card details.<br><br>**Constraints**: *Maximum Length*: `40000` |
| `encrypted_card_number` | `str` | Optional | The encrypted card number.<br><br>**Constraints**: *Maximum Length*: `15000` |
| `encrypted_expiry_month` | `str` | Optional | The encrypted card expiry month.<br><br>**Constraints**: *Maximum Length*: `15000` |
| `encrypted_expiry_year` | `str` | Optional | The encrypted card expiry year.<br><br>**Constraints**: *Maximum Length*: `15000` |
| `encrypted_password` | `str` | Optional | This field contains an encrypted, one-time password or an authentication code provided by the cardholder.<br><br>**Constraints**: *Maximum Length*: `15000` |
| `encrypted_security_code` | `str` | Optional | The encrypted card verification code.<br><br>**Constraints**: *Maximum Length*: `15000` |
| `expiry_month` | `str` | Optional | The card expiry month. Only collect raw card data if you are [fully PCI compliant](https://docs.adyen.com/development-resources/pci-dss-compliance-guide). |
| `expiry_year` | `str` | Optional | The card expiry year. Only collect raw card data if you are [fully PCI compliant](https://docs.adyen.com/development-resources/pci-dss-compliance-guide). |
| `fastlane_data` | `str` | Optional | The encoded fastlane data blob |
| `funding_source` | [`FundingSource`](../../doc/models/funding-source.md) | Optional | - |
| `holder_name` | `str` | Optional | The name of the card holder.<br><br>**Constraints**: *Maximum Length*: `15000` |
| `network_payment_reference` | `str` | Optional | The transaction identifier from card schemes. This is the [`networkTxReference`](https://docs.adyen.com/api-explorer/Checkout/latest/post/payments#responses-200-additionalData-ResponseAdditionalDataCommon-networkTxReference) from the response to the first payment. |
| `number` | `str` | Optional | The card number. Only collect raw card data if you are [fully PCI compliant](https://docs.adyen.com/development-resources/pci-dss-compliance-guide). |
| `recurring_detail_reference` | `str` | Optional | This is the `recurringDetailReference` returned in the response when you created the token. |
| `sdk_data` | `str` | Optional | Base64-encoded JSON object containing SDK related parameters required by the SDK<br><br>**Constraints**: *Maximum Length*: `50000` |
| `shopper_notification_reference` | `str` | Optional | The `shopperNotificationReference` returned in the response when you requested to notify the shopper. Used only for recurring payments in India. |
| `src_correlation_id` | `str` | Optional | An identifier used for the Click to Pay transaction. |
| `src_digital_card_id` | `str` | Optional | The SRC reference for the Click to Pay token. |
| `src_scheme` | `str` | Optional | The scheme that is being used for Click to Pay. |
| `src_token_reference` | `str` | Optional | The reference for the Click to Pay token. |
| `stored_payment_method_id` | `str` | Optional | This is the `recurringDetailReference` returned in the response when you created the token.<br><br>**Constraints**: *Maximum Length*: `64` |
| `three_ds_2_sdk_version` | `str` | Optional | Required for mobile integrations. Version of the 3D Secure 2 mobile SDK.<br><br>**Constraints**: *Maximum Length*: `12` |
| `mtype` | [`Type141`](../../doc/models/type-141.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.card_donations import CardDonations

card_donations = CardDonations(
    billing_sequence_number='billingSequenceNumber4',
    brand='brand8',
    checkout_attempt_id='checkoutAttemptId0',
    cupsecureplus_smscode='cupsecureplus.smscode2',
    cvc='cvc8',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

