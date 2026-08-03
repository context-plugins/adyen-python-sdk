
# Installments 2

*This model accepts additional fields of type Any.*

## Structure

`Installments2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `extra` | `int` | Optional | Defines the bonus percentage, refund percentage or if the transaction is Buy now Pay later.<br>Used for [card installments in Mexico](https://docs.adyen.com/payment-methods/cards/credit-card-installments/#getting-paid-mexico) |
| `plan` | [`Plan`](../../doc/models/plan.md) | Optional | - |
| `value` | `int` | Required | Defines the number of installments.<br>Usually, the maximum allowed number of installments is capped. For example, it may not be possible to split a payment in more than 24 installments. The acquirer sets this upper limit, so its value may vary.<br>This value can be zero for Installments processed in Mexico. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.installments_2 import Installments2
from adyen.models.plan import Plan

installments_2 = Installments2(
    value=24,
    extra=84,
    plan=Plan.BONUS,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

