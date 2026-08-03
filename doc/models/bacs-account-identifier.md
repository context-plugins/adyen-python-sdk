
# Bacs Account Identifier

*This model accepts additional fields of type Any.*

## Structure

`BacsAccountIdentifier`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_number` | `str` | Required | The account number of the bank account. |
| `sort_code` | `str` | Required | A number that identifies the specific bank and branch where a UK bank account is held. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.bacs_account_identifier import BacsAccountIdentifier

bacs_account_identifier = BacsAccountIdentifier(
    account_number='accountNumber2',
    sort_code='sortCode2',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

