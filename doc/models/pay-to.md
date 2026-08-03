
# Pay To

*This model accepts additional fields of type Any.*

## Structure

`PayTo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `checkout_attempt_id` | `str` | Optional | The checkout attempt identifier. |
| `recurring_detail_reference` | `str` | Optional | This is the `recurringDetailReference` returned in the response when you created the token. |
| `sdk_data` | `str` | Optional | Base64-encoded JSON object containing SDK related parameters required by the SDK<br><br>**Constraints**: *Maximum Length*: `50000` |
| `shopper_account_identifier` | `str` | Optional | The shopper's banking details or payId reference, used to complete payment. |
| `stored_payment_method_id` | `str` | Optional | This is the `recurringDetailReference` returned in the response when you created the token.<br><br>**Constraints**: *Maximum Length*: `64` |
| `mtype` | [`Type411`](../../doc/models/type-411.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.pay_to import PayTo

pay_to = PayTo(
    checkout_attempt_id='checkoutAttemptId2',
    recurring_detail_reference='recurringDetailReference6',
    sdk_data='sdkData4',
    shopper_account_identifier='shopperAccountIdentifier6',
    stored_payment_method_id='storedPaymentMethodId0',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

