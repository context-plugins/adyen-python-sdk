
# Eft Account Identifier

*This model accepts additional fields of type Any.*

## Structure

`EftAccountIdentifier`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_number` | `str` | Required | The account number of the bank account. |
| `branch` | `str` | Required | Identifies the specific branch where the account is held within the Canadian banking system. |
| `institution` | `str` | Required | The financial institution that identifies the bank in Canada. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.eft_account_identifier import EftAccountIdentifier

eft_account_identifier = EftAccountIdentifier(
    account_number='accountNumber2',
    branch='branch0',
    institution='institution4',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

