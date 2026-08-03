
# Bsb Account Identifier 2

Identifiers relevant for Australian banking, specifically for BSB (Bank-State-Branch) numbers.

*This model accepts additional fields of type Any.*

## Structure

`BsbAccountIdentifier2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_number` | `str` | Required | The account number of the bank account. |
| `bsb_code` | `str` | Required | The BSB (Bank-State-Branch) code. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.bsb_account_identifier_2 import BsbAccountIdentifier2

bsb_account_identifier_2 = BsbAccountIdentifier2(
    account_number='accountNumber2',
    bsb_code='bsbCode4',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

