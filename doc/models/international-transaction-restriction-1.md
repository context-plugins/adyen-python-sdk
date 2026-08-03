
# International Transaction Restriction 1

Indicates whether transaction is an international transaction and specifies the operation.

Supported operations: **equals**, **notEquals**.

*This model accepts additional fields of type Any.*

## Structure

`InternationalTransactionRestriction1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `operation` | `str` | Required | Defines how the condition must be evaluated. |
| `value` | `bool` | Optional | Boolean indicating whether transaction is an international transaction.<br><br>Possible values:<br><br>- **true**: The transaction is an international transaction.<br><br>- **false**: The transaction is a domestic transaction. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.international_transaction_restriction_1 import InternationalTransactionRestriction1

international_transaction_restriction_1 = InternationalTransactionRestriction1(
    operation='operation6',
    value=False,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

