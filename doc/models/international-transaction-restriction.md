
# International Transaction Restriction

## Structure

`InternationalTransactionRestriction`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `operation` | `str` | Required | Defines how the condition must be evaluated. |
| `value` | `bool` | Optional | Boolean indicating whether transaction is an international transaction.<br><br>Possible values:<br><br>- **true**: The transaction is an international transaction.<br><br>- **false**: The transaction is a domestic transaction. |

## Example

```python
from adyen.models.international_transaction_restriction import InternationalTransactionRestriction

international_transaction_restriction = InternationalTransactionRestriction(
    operation='operation2',
    value=False
)
```

