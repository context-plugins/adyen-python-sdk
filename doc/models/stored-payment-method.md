
# Stored Payment Method

*This model accepts additional fields of type Any.*

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
| `mtype` | [`Type16`](../../doc/models/type-16.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.stored_payment_method import StoredPaymentMethod

stored_payment_method = StoredPaymentMethod(
    cashtag='cashtag6',
    checkout_attempt_id='checkoutAttemptId4',
    customer_id='customerId2',
    grant_id='grantId6',
    on_file_grant_id='onFileGrantId6',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

