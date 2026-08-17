
# BSB Account Identifier 2

Identifiers relevant for Australian banking, specifically for BSB (Bank-State-Branch) numbers.

## Structure

`BSBAccountIdentifier2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_number` | `str` | Required | The account number of the bank account. |
| `bsb_code` | `str` | Required | The BSB (Bank-State-Branch) code. |

## Example

```python
from adyen.models.bsb_account_identifier_2 import BSBAccountIdentifier2

bsb_account_identifier_2 = BSBAccountIdentifier2(
    account_number='accountNumber2',
    bsb_code='bsbCode4'
)
```

