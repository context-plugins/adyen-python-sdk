
# Different Currencies Restriction

## Structure

`DifferentCurrenciesRestriction`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `operation` | `str` | Required | Defines how the condition must be evaluated. |
| `value` | `bool` | Optional | Checks the currency of the payment against the currency of the payment instrument.<br><br>Possible values:<br><br>- **true**: The currency of the payment is different from the currency of the payment instrument.<br><br>- **false**: The currencies are the same. |

## Example

```python
from adyen.models.different_currencies_restriction import DifferentCurrenciesRestriction

different_currencies_restriction = DifferentCurrenciesRestriction(
    operation='operation0',
    value=False
)
```

