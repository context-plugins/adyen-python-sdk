
# HK Local Account Identification 1

## Structure

`HKLocalAccountIdentification1`

## Inherits From

[`BankAccountIdentification`](../../doc/models/bank-account-identification.md)

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_number` | `str` | Required | The 9- to 17-digit bank account number, without separators or whitespace. Starts with the 3-digit branch code.<br><br>**Constraints**: *Minimum Length*: `9`, *Maximum Length*: `17` |
| `clearing_code` | `str` | Required | The 3-digit clearing code, without separators or whitespace.<br><br>**Constraints**: *Minimum Length*: `3`, *Maximum Length*: `3` |

## Example

```python
from adyen.models.bank_account_identification import HKLocalAccountIdentification1

hk_local_account_identification_1 = HKLocalAccountIdentification1(
    account_number='accountNumber2',
    clearing_code='clearingCode8',
    mtype='hkLocal'
)
```

