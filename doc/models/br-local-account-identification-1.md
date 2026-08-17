
# BR Local Account Identification 1

## Structure

`BRLocalAccountIdentification1`

## Inherits From

[`BankAccountIdentification`](../../doc/models/bank-account-identification.md)

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_number` | `str` | Required | The bank account number, without separators or whitespace.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `10` |
| `bank_code` | `str` | Required | The 3-digit bank code, with leading zeros.<br><br>**Constraints**: *Minimum Length*: `3`, *Maximum Length*: `3` |
| `branch_number` | `str` | Required | The bank account branch number, without separators or whitespace.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `4` |
| `ispb` | `str` | Optional | The 8-digit ISPB, with leading zeros.<br><br>**Constraints**: *Minimum Length*: `8`, *Maximum Length*: `8` |

## Example

```python
from adyen.models.bank_account_identification import BRLocalAccountIdentification1

br_local_account_identification_1 = BRLocalAccountIdentification1(
    account_number='accountNumber2',
    bank_code='bankCode0',
    branch_number='branchNumber0',
    ispb='ispb4',
    mtype='brLocal'
)
```

