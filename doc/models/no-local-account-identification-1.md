
# NO Local Account Identification 1

## Structure

`NOLocalAccountIdentification1`

## Inherits From

[`BankAccountIdentification`](../../doc/models/bank-account-identification.md)

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_number` | `str` | Required | The 11-digit bank account number, without separators or whitespace.<br><br>**Constraints**: *Minimum Length*: `11`, *Maximum Length*: `11` |

## Example

```python
from adyen.models.bank_account_identification import NOLocalAccountIdentification1

no_local_account_identification_1 = NOLocalAccountIdentification1(
    account_number='accountNumber4',
    mtype='noLocal'
)
```

