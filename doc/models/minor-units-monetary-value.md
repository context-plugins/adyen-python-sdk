
# Minor Units Monetary Value

## Structure

`MinorUnitsMonetaryValue`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amount` | `int` | Optional | The transaction amount, in [minor units](https://docs.adyen.com/development-resources/currency-codes). |
| `currency_code` | `str` | Optional | The three-character [ISO currency code](https://docs.adyen.com/development-resources/currency-codes). |

## Example

```python
from adyen.models.minor_units_monetary_value import MinorUnitsMonetaryValue

minor_units_monetary_value = MinorUnitsMonetaryValue(
    amount=122,
    currency_code='currencyCode8'
)
```

