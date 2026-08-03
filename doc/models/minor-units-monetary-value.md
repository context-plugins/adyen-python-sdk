
# Minor Units Monetary Value

*This model accepts additional fields of type Any.*

## Structure

`MinorUnitsMonetaryValue`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amount` | `int` | Optional | The transaction amount, in [minor units](https://docs.adyen.com/development-resources/currency-codes). |
| `currency_code` | `str` | Optional | The three-character [ISO currency code](https://docs.adyen.com/development-resources/currency-codes). |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.minor_units_monetary_value import MinorUnitsMonetaryValue

minor_units_monetary_value = MinorUnitsMonetaryValue(
    amount=122,
    currency_code='currencyCode8',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

