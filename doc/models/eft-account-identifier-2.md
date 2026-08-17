
# EFT Account Identifier 2

Identifiers relevant for Electronic Funds Transfer (EFT) payments, commonly used in Canada.

## Structure

`EFTAccountIdentifier2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_number` | `str` | Required | The account number of the bank account. |
| `branch` | `str` | Required | Identifies the specific branch where the account is held within the Canadian banking system. |
| `institution` | `str` | Required | The financial institution that identifies the bank in Canada. |

## Example

```python
from adyen.models.eft_account_identifier_2 import EFTAccountIdentifier2

eft_account_identifier_2 = EFTAccountIdentifier2(
    account_number='accountNumber0',
    branch='branch8',
    institution='institution2'
)
```

