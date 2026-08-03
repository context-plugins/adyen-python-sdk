
# Eft Account Identifier 2

Identifiers relevant for Electronic Funds Transfer (EFT) payments, commonly used in Canada.

*This model accepts additional fields of type Any.*

## Structure

`EftAccountIdentifier2`

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

from adyen.models.eft_account_identifier_2 import EftAccountIdentifier2

eft_account_identifier_2 = EftAccountIdentifier2(
    account_number='accountNumber0',
    branch='branch8',
    institution='institution2',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

