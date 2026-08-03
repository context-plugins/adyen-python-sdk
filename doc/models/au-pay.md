
# Au Pay

*This model accepts additional fields of type Any.*

## Structure

`AuPay`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `checkout_attempt_id` | `str` | Optional | The checkout attempt identifier. |
| `recurring_detail_reference` | `str` | Optional | This is the `recurringDetailReference` returned in the response when you created the token. |
| `sdk_data` | `str` | Optional | Base64-encoded JSON object containing SDK related parameters required by the SDK<br><br>**Constraints**: *Maximum Length*: `50000` |
| `stored_payment_method_id` | `str` | Optional | This is the `recurringDetailReference` returned in the response when you created the token.<br><br>**Constraints**: *Maximum Length*: `64` |
| `mtype` | [`Type91`](../../doc/models/type-91.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.au_pay import AuPay
from adyen.models.type_91 import Type91

au_pay = AuPay(
    checkout_attempt_id='checkoutAttemptId2',
    recurring_detail_reference='recurringDetailReference6',
    sdk_data='sdkData4',
    stored_payment_method_id='storedPaymentMethodId0',
    mtype=Type91.AUPAY,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

