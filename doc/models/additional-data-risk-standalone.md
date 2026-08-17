
# Additional Data Risk Standalone

## Structure

`AdditionalDataRiskStandalone`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `pay_pal_country_code` | `str` | Optional | Shopper's country of residence in the form of ISO standard 3166 2-character country codes. |
| `pay_pal_email_id` | `str` | Optional | Shopper's email. |
| `pay_pal_first_name` | `str` | Optional | Shopper's first name. |
| `pay_pal_last_name` | `str` | Optional | Shopper's last name. |
| `pay_pal_payer_id` | `str` | Optional | Unique PayPal Customer Account identification number. Character length and limitations: 13 single-byte alphanumeric characters. |
| `pay_pal_phone` | `str` | Optional | Shopper's phone number. |
| `pay_pal_protection_eligibility` | `str` | Optional | Allowed values:<br><br>* **Eligible** — Merchant is protected by PayPal's Seller Protection Policy for Unauthorized Payments and Item Not Received.<br><br>* **PartiallyEligible** — Merchant is protected by PayPal's Seller Protection Policy for Item Not Received.<br><br>* **Ineligible** — Merchant is not protected under the Seller Protection Policy. |
| `pay_pal_transaction_id` | `str` | Optional | Unique transaction ID of the payment. |
| `avs_result_raw` | `str` | Optional | Raw AVS result received from the acquirer, where available. Example: D |
| `bin` | `str` | Optional | The Bank Identification Number of a credit card, which is the first six digits of a card number. Required for [tokenized card request](https://docs.adyen.com/online-payments/tokenization). |
| `cvc_result_raw` | `str` | Optional | Raw CVC result received from the acquirer, where available. Example: 1 |
| `risk_token` | `str` | Optional | Unique identifier or token for the shopper's card details. |
| `three_d_authenticated` | `str` | Optional | A Boolean value indicating whether 3DS authentication was completed on this payment. Example: true |
| `three_d_offered` | `str` | Optional | A Boolean value indicating whether 3DS was offered for this payment. Example: true |
| `token_data_type` | `str` | Optional | Required for PayPal payments only. The only supported value is: **paypal**. |

## Example

```python
from adyen.models.additional_data_risk_standalone import AdditionalDataRiskStandalone

additional_data_risk_standalone = AdditionalDataRiskStandalone(
    pay_pal_country_code='PayPal.CountryCode2',
    pay_pal_email_id='PayPal.EmailId2',
    pay_pal_first_name='PayPal.FirstName6',
    pay_pal_last_name='PayPal.LastName2',
    pay_pal_payer_id='PayPal.PayerId4'
)
```

