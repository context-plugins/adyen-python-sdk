
# UK Local Mandate Account Identification

## Structure

`UKLocalMandateAccountIdentification`

## Inherits From

[`MandateAccountIdentification`](../../doc/models/mandate-account-identification.md)

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_number` | `str` | Required | The 8-digit bank account number, without separators or whitespace.<br><br>**Constraints**: *Minimum Length*: `8`, *Maximum Length*: `8` |
| `sort_code` | `str` | Required | The 6-digit [sort code](https://en.wikipedia.org/wiki/Sort_code), without separators or whitespace.<br><br>**Constraints**: *Minimum Length*: `6`, *Maximum Length*: `6` |

## Example

```python
from adyen.models.mandate_account_identification import UKLocalMandateAccountIdentification

uk_local_mandate_account_identification = UKLocalMandateAccountIdentification(
    account_number='accountNumber4',
    sort_code='sortCode6',
    mtype='ukLocal'
)
```

