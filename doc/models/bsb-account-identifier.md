
# Bsb Account Identifier

*This model accepts additional fields of type Any.*

## Structure

`BsbAccountIdentifier`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_number` | `str` | Required | The account number of the bank account. |
| `bsb_code` | `str` | Required | The BSB (Bank-State-Branch) code. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.bsb_account_identifier import BsbAccountIdentifier

bsb_account_identifier = BsbAccountIdentifier(
    account_number='accountNumber0',
    bsb_code='bsbCode2',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

