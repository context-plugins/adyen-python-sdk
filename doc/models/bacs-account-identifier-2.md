
# Bacs Account Identifier 2

Identifiers relevant for Bankers' Automated Clearing Services (BACS) payments, primarily used in the United Kingdom.

*This model accepts additional fields of type Any.*

## Structure

`BacsAccountIdentifier2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_number` | `str` | Required | The account number of the bank account. |
| `sort_code` | `str` | Required | A number that identifies the specific bank and branch where a UK bank account is held. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.bacs_account_identifier_2 import BacsAccountIdentifier2

bacs_account_identifier_2 = BacsAccountIdentifier2(
    account_number='accountNumber4',
    sort_code='sortCode6',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

