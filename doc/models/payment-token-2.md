
# Payment Token 2

*This model accepts additional fields of type Any.*

## Structure

`PaymentToken2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `token_requested_type` | [`TokenRequestedType1`](../../doc/models/token-requested-type-1.md) | Required | - |
| `token_value` | `str` | Required | Payment token replacing the PAN of the payment card to identify the payment<br>mean of the customer.<br><br>**Constraints**: *Pattern*: `^.+$` |
| `expiry_date_time` | `datetime` | Optional | Expiry date and time. Limits the validity of a payment token. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from adyen.models.payment_token_2 import PaymentToken2
from adyen.models.token_requested_type_1 import TokenRequestedType1

payment_token_2 = PaymentToken2(
    token_requested_type=TokenRequestedType1.TRANSACTION,
    token_value='TokenValue8',
    expiry_date_time=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

