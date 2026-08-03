
# Converted Amount 1

Amount after a currency conversion.

*This model accepts additional fields of type Any.*

## Structure

`ConvertedAmount1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amount_value` | `float` | Required | Value of an amount.<br><br>**Constraints**: `>= 0`, `<= 99999999.999999` |
| `currency` | `str` | Required | Currency of a monetary amount.<br><br>**Constraints**: *Pattern*: `^[A-Z]{3,3}$` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.converted_amount_1 import ConvertedAmount1

converted_amount_1 = ConvertedAmount1(
    amount_value=184.32,
    currency='Currency0',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

