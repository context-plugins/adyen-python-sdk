
# HU Local Account Identification 1

## Structure

`HULocalAccountIdentification1`

## Inherits From

[`BankAccountIdentification`](../../doc/models/bank-account-identification.md)

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_number` | `str` | Required | The 24-digit bank account number, without separators or whitespace.<br><br>**Constraints**: *Minimum Length*: `24`, *Maximum Length*: `24` |

## Example

```python
from adyen.models.bank_account_identification import HULocalAccountIdentification1

hu_local_account_identification_1 = HULocalAccountIdentification1(
    account_number='accountNumber2',
    mtype='huLocal'
)
```

