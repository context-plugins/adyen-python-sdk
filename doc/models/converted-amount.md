
# Converted Amount

*This model accepts additional fields of type Any.*

## Structure

`ConvertedAmount`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amount_value` | `float` | Required | Value of an amount.<br><br>**Constraints**: `>= 0`, `<= 99999999.999999` |
| `currency` | `str` | Required | Currency of a monetary amount.<br><br>**Constraints**: *Pattern*: `^[A-Z]{3,3}$` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.converted_amount import ConvertedAmount

converted_amount = ConvertedAmount(
    amount_value=50.14,
    currency='Currency2',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

