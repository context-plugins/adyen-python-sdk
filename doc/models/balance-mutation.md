
# Balance Mutation

*This model accepts additional fields of type Any.*

## Structure

`BalanceMutation`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `balance` | `int` | Optional | The amount in the payment's currency that is debited or credited on the balance accounting register. |
| `currency` | `str` | Optional | The three-character [ISO currency code](https://docs.adyen.com/development-resources/currency-codes). |
| `received` | `int` | Optional | The amount in the payment's currency that is debited or credited on the received accounting register. |
| `reserved` | `int` | Optional | The amount in the payment's currency that is debited or credited on the reserved accounting register. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.balance_mutation import BalanceMutation

balance_mutation = BalanceMutation(
    balance=68,
    currency='currency4',
    received=114,
    reserved=2,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

