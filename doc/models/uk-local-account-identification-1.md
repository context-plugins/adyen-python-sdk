
# UK Local Account Identification 1

## Structure

`UKLocalAccountIdentification1`

## Inherits From

[`BankAccountIdentification`](../../doc/models/bank-account-identification.md)

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_number` | `str` | Required | The 8-digit bank account number, without separators or whitespace.<br><br>**Constraints**: *Minimum Length*: `8`, *Maximum Length*: `8` |
| `sort_code` | `str` | Required | The 6-digit [sort code](https://en.wikipedia.org/wiki/Sort_code), without separators or whitespace.<br><br>**Constraints**: *Minimum Length*: `6`, *Maximum Length*: `6` |

## Example

```python
from adyen.models.bank_account_identification import UKLocalAccountIdentification1

uk_local_account_identification_1 = UKLocalAccountIdentification1(
    account_number='accountNumber0',
    sort_code='sortCode0',
    mtype='ukLocal'
)
```

