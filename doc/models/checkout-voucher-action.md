
# Checkout Voucher Action

*This model accepts additional fields of type Any.*

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
| `initial_amount` | [`InitialAmount`](../../doc/models/initial-amount.md) | Optional | - |
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
| `surcharge` | [`Surcharge5`](../../doc/models/surcharge-5.md) | Optional | - |
| `total_amount` | [`TotalAmount2`](../../doc/models/total-amount-2.md) | Optional | - |
| `mtype` | [`Type594`](../../doc/models/type-594.md) | Required | **voucher** |
| `url` | `str` | Optional | Specifies the URL to redirect to. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.checkout_voucher_action import CheckoutVoucherAction
from adyen.models.type_594 import Type594

checkout_voucher_action = CheckoutVoucherAction(
    mtype=Type594.VOUCHER,
    alternative_reference='alternativeReference2',
    collection_institution_number='collectionInstitutionNumber6',
    download_url='downloadUrl6',
    entity='entity2',
    expires_at='expiresAt0',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

