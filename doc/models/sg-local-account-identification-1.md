
# SG Local Account Identification 1

## Structure

`SGLocalAccountIdentification1`

## Inherits From

[`BankAccountIdentification`](../../doc/models/bank-account-identification.md)

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_number` | `str` | Required | The 4- to 19-digit bank account number, without separators or whitespace.<br><br>**Constraints**: *Minimum Length*: `4`, *Maximum Length*: `19` |
| `bic` | `str` | Required | The bank's 8- or 11-character BIC or SWIFT code.<br><br>**Constraints**: *Minimum Length*: `8`, *Maximum Length*: `11` |

## Example

```python
from adyen.models.bank_account_identification import SGLocalAccountIdentification1

sg_local_account_identification_1 = SGLocalAccountIdentification1(
    account_number='accountNumber8',
    bic='bic6',
    mtype='sgLocal'
)
```

