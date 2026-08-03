
# Amounts 1

The object that contains the fixed donation amounts that the shopper can select from.

*This model accepts additional fields of type Any.*

## Structure

`Amounts1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `currency` | `str` | Required | The three-character [ISO currency code](https://docs.adyen.com/development-resources/currency-codes/). |
| `values` | `List[int]` | Required | The amounts of the donation (in [minor units](https://docs.adyen.com/development-resources/currency-codes/)). |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.amounts_1 import Amounts1

amounts_1 = Amounts1(
    currency='currency0',
    values=[
        252,
        253
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

