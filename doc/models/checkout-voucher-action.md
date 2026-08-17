
# Checkout Voucher Action

## Structure

`CheckoutVoucherAction`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `alternative_reference` | `str` | Optional | The voucher alternative reference code. |
| `collection_institution_number` | `str` | Optional | A collection institution number (store number) for Econtext Pay-Easy ATM. |
| `download_url` | `str` | Optional | The URL to download the voucher. |
| `entity` | `str` | Optional | An entity number of Multibanco. |
| `expires_at` | `str` | Optional | The date time of the voucher expiry. |
| `initial_amount` | [`Amount14`](../../doc/models/amount-14.md) | Optional | The initial amount. |
| `instructions_url` | `str` | Optional | The URL to the detailed instructions to make payment using the voucher. |
| `issuer` | `str` | Optional | The issuer of the voucher. |
| `masked_telephone_number` | `str` | Optional | The shopper telephone number (partially masked). |
| `merchant_name` | `str` | Optional | The merchant name. |
| `merchant_reference` | `str` | Optional | The merchant reference. |
| `pass_creation_token` | `str` | Optional | A Base64-encoded token containing all properties of the voucher. For iOS, you can use this to pass a voucher to Apple Wallet. |
| `payment_data` | `str` | Optional | Encoded payment data. |
| `payment_method_type` | `str` | Optional | Specifies the payment method. |
| `reference` | `str` | Optional | The voucher reference code. |
| `shopper_email` | `str` | Optional | The shopper email. |
| `shopper_name` | `str` | Optional | The shopper name. |
| `surcharge` | [`Amount15`](../../doc/models/amount-15.md) | Optional | The surcharge amount. |
| `total_amount` | [`Amount16`](../../doc/models/amount-16.md) | Optional | The total amount (initial plus surcharge amount). |
| `mtype` | `str` | Required, Constant | **voucher**<br><br>**Value**: `"voucher"` |
| `url` | `str` | Optional | Specifies the URL to redirect to. |

## Example

```python
from adyen.models.checkout_voucher_action import CheckoutVoucherAction

checkout_voucher_action = CheckoutVoucherAction(
    alternative_reference='alternativeReference2',
    collection_institution_number='collectionInstitutionNumber6',
    download_url='downloadUrl6',
    entity='entity2',
    expires_at='expiresAt0'
)
```

