
# BSB Account Identifier

## Structure

`BSBAccountIdentifier`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_number` | `str` | Required | The account number of the bank account. |
| `bsb_code` | `str` | Required | The BSB (Bank-State-Branch) code. |

## Example

```python
from adyen.models.bsb_account_identifier import BSBAccountIdentifier

bsb_account_identifier = BSBAccountIdentifier(
    account_number='accountNumber0',
    bsb_code='bsbCode2'
)
```

