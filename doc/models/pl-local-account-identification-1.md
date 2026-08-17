
# PL Local Account Identification 1

## Structure

`PLLocalAccountIdentification1`

## Inherits From

[`BankAccountIdentification`](../../doc/models/bank-account-identification.md)

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_number` | `str` | Required | The 26-digit bank account number ([Numer rachunku](https://pl.wikipedia.org/wiki/Numer_Rachunku_Bankowego)), without separators or whitespace.<br><br>**Constraints**: *Minimum Length*: `26`, *Maximum Length*: `26` |

## Example

```python
from adyen.models.bank_account_identification import PLLocalAccountIdentification1

pl_local_account_identification_1 = PLLocalAccountIdentification1(
    account_number='accountNumber6',
    mtype='plLocal'
)
```

