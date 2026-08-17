
# EFT Account Identifier

## Structure

`EFTAccountIdentifier`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_number` | `str` | Required | The account number of the bank account. |
| `branch` | `str` | Required | Identifies the specific branch where the account is held within the Canadian banking system. |
| `institution` | `str` | Required | The financial institution that identifies the bank in Canada. |

## Example

```python
from adyen.models.eft_account_identifier import EFTAccountIdentifier

eft_account_identifier = EFTAccountIdentifier(
    account_number='accountNumber2',
    branch='branch0',
    institution='institution4'
)
```

