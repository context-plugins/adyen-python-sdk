
# Capital Balance

Contains information about the balances of the disbursement.

*This model accepts additional fields of type Any.*

## Structure

`CapitalBalance`

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

from adyen.models.capital_balance import CapitalBalance

capital_balance = CapitalBalance(
    currency='currency0',
    fee=236,
    principal=18,
    total=198,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

