
# Rix Account Identifier

*This model accepts additional fields of type Any.*

## Structure

`RixAccountIdentifier`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_number` | `str` | Required | The account number of the bank account. |
| `clearing_number` | `str` | Required | The 4- to 5-digit clearing number, without separators or whitespace. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.rix_account_identifier import RixAccountIdentifier

rix_account_identifier = RixAccountIdentifier(
    account_number='accountNumber4',
    clearing_number='clearingNumber8',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

