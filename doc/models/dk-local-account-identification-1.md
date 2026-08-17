
# DK Local Account Identification 1

## Structure

`DKLocalAccountIdentification1`

## Inherits From

[`BankAccountIdentification`](../../doc/models/bank-account-identification.md)

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_number` | `str` | Required | The 4-10 digits bank account number (Kontonummer) (without separators or whitespace).<br><br>**Constraints**: *Minimum Length*: `4`, *Maximum Length*: `10` |
| `bank_code` | `str` | Required | The 4-digit bank code (Registreringsnummer) (without separators or whitespace).<br><br>**Constraints**: *Minimum Length*: `4`, *Maximum Length*: `4` |

## Example

```python
from adyen.models.bank_account_identification import DKLocalAccountIdentification1

dk_local_account_identification_1 = DKLocalAccountIdentification1(
    account_number='accountNumber2',
    bank_code='bankCode4',
    mtype='dkLocal'
)
```

