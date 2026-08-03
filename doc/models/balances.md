
# Balances

*This model accepts additional fields of type Any.*

## Structure

`Balances`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `currency` | `str` | Required | The three-character [ISO currency code](https://docs.adyen.com/development-resources/currency-codes). |
| `fee` | `int` | Required | Fee amount. |
| `principal` | `int` | Required | Principal amount. |
| `total` | `int` | Required | Total amount. A sum of principal amount and fee amount. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.balances import Balances

balances = Balances(
    currency='currency0',
    fee=72,
    principal=110,
    total=150,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

