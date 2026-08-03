
# Zip

*This model accepts additional fields of type Any.*

## Structure

`Zip`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `checkout_attempt_id` | `str` | Optional | The checkout attempt identifier. |
| `click_and_collect` | `str` | Optional | Set this to **true** if the shopper would like to pick up and collect their order, instead of having the goods delivered to them. |
| `recurring_detail_reference` | `str` | Optional | This is the `recurringDetailReference` returned in the response when you created the token. |
| `sdk_data` | `str` | Optional | Base64-encoded JSON object containing SDK related parameters required by the SDK<br><br>**Constraints**: *Maximum Length*: `50000` |
| `stored_payment_method_id` | `str` | Optional | This is the `recurringDetailReference` returned in the response when you created the token.<br><br>**Constraints**: *Maximum Length*: `64` |
| `mtype` | [`Type58`](../../doc/models/type-58.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.zip import Zip

zip = Zip(
    checkout_attempt_id='checkoutAttemptId2',
    click_and_collect='clickAndCollect6',
    recurring_detail_reference='recurringDetailReference6',
    sdk_data='sdkData4',
    stored_payment_method_id='storedPaymentMethodId0',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

