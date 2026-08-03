
# Payment Token 1

Surrogate of the PAN (Primary Account Number) of the payment card to identify the payment mean of the customer. It allows, for a merchant, to identify the customer.
Restriction of product payable by a card.

*This model accepts additional fields of type Any.*

## Structure

`PaymentToken1`

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

from adyen.models.payment_token_1 import PaymentToken1
from adyen.models.token_requested_type_1 import TokenRequestedType1

payment_token_1 = PaymentToken1(
    token_requested_type=TokenRequestedType1.TRANSACTION,
    token_value='TokenValue2',
    expiry_date_time=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

