
# Stored Payment Method

## Structure

`StoredPaymentMethod`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `cashtag` | `str` | Optional | Cash App issued cashtag for recurring payment |
| `checkout_attempt_id` | `str` | Optional | The checkout attempt identifier. |
| `customer_id` | `str` | Optional | Cash App issued customerId for recurring payment |
| `grant_id` | `str` | Optional | Cash App issued grantId for one time payment |
| `on_file_grant_id` | `str` | Optional | Cash App issued onFileGrantId for recurring payment |
| `recurring_detail_reference` | `str` | Optional | This is the `recurringDetailReference` returned in the response when you created the token. |
| `request_id` | `str` | Optional | Cash App request id |
| `sdk_data` | `str` | Optional | Base64-encoded JSON object containing SDK related parameters required by the SDK<br><br>**Constraints**: *Maximum Length*: `50000` |
| `stored_payment_method_id` | `str` | Optional | This is the `recurringDetailReference` returned in the response when you created the token.<br><br>**Constraints**: *Maximum Length*: `64` |
| `subtype` | `str` | Optional | The payment method subtype. |
| `mtype` | [`Type16Enum`](../../doc/models/type-16-enum.md) | Optional | cashapp<br><br>**Default**: `"cashapp"` |

## Example

```python
from adyen.models.stored_payment_method import StoredPaymentMethod
from adyen.models.type_16_enum import Type16Enum

stored_payment_method = StoredPaymentMethod(
    cashtag='cashtag6',
    checkout_attempt_id='checkoutAttemptId4',
    customer_id='customerId2',
    grant_id='grantId6',
    on_file_grant_id='onFileGrantId6',
    mtype=Type16Enum.CASHAPP
)
```

