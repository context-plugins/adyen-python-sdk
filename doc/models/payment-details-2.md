
# Payment Details 2

*This model accepts additional fields of type Any.*

## Structure

`PaymentDetails2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `checkout_attempt_id` | `str` | Optional | The checkout attempt identifier. |
| `sdk_data` | `str` | Optional | Base64-encoded JSON object containing SDK related parameters required by the SDK<br><br>**Constraints**: *Maximum Length*: `50000` |
| `mtype` | [`Type43`](../../doc/models/type-43.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.payment_details_2 import PaymentDetails2
from adyen.models.type_43 import Type43

payment_details_2 = PaymentDetails2(
    checkout_attempt_id='checkoutAttemptId2',
    sdk_data='sdkData4',
    mtype=Type43.FACILYPAY_6X,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

