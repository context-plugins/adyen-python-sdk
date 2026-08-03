
# Rix Account Identifier 2

Identifiers relevant for the Rix (Russian Interbank eXchange) system, used for interbank payments within Russia.

*This model accepts additional fields of type Any.*

## Structure

`RixAccountIdentifier2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_number` | `str` | Required | The account number of the bank account. |
| `clearing_number` | `str` | Required | The 4- to 5-digit clearing number, without separators or whitespace. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.rix_account_identifier_2 import RixAccountIdentifier2

rix_account_identifier_2 = RixAccountIdentifier2(
    account_number='accountNumber6',
    clearing_number='clearingNumber6',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

