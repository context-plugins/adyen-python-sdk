
# Different Currencies Restriction 1

Compares the currency of the payment against the currency of the payment instrument, and specifies the operation.

Supported operations: **equals**, **notEquals**.

*This model accepts additional fields of type Any.*

## Structure

`DifferentCurrenciesRestriction1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `operation` | `str` | Required | Defines how the condition must be evaluated. |
| `value` | `bool` | Optional | Checks the currency of the payment against the currency of the payment instrument.<br><br>Possible values:<br><br>- **true**: The currency of the payment is different from the currency of the payment instrument.<br><br>- **false**: The currencies are the same. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.different_currencies_restriction_1 import DifferentCurrenciesRestriction1

different_currencies_restriction_1 = DifferentCurrenciesRestriction1(
    operation='operation0',
    value=False,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

