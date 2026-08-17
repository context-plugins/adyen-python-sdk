
# AU Local Account Identification 1

## Structure

`AULocalAccountIdentification1`

## Inherits From

[`BankAccountIdentification`](../../doc/models/bank-account-identification.md)

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_number` | `str` | Required | The bank account number, without separators or whitespace.<br><br>**Constraints**: *Minimum Length*: `5`, *Maximum Length*: `9` |
| `bsb_code` | `str` | Required | The 6-digit [Bank State Branch (BSB) code](https://en.wikipedia.org/wiki/Bank_state_branch), without separators or whitespace.<br><br>**Constraints**: *Minimum Length*: `6`, *Maximum Length*: `6` |

## Example

```python
from adyen.models.bank_account_identification import AULocalAccountIdentification1

au_local_account_identification_1 = AULocalAccountIdentification1(
    account_number='accountNumber8',
    bsb_code='bsbCode0',
    mtype='auLocal'
)
```

