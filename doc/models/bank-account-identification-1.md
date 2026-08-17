
# Bank Account Identification 1

Contains the identification information of the account to which you can transfer funds related to repayments.

## Structure

`BankAccountIdentification1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | `str` | Optional | - |

## Example

```python
from adyen.models.bank_account_identification_1 import BankAccountIdentification1

bank_account_identification_1 = BankAccountIdentification1(
    mtype='BankAccountIdentification1'
)
```

