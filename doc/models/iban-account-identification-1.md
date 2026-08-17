
# Iban Account Identification 1

## Structure

`IbanAccountIdentification1`

## Inherits From

[`BankAccountIdentification`](../../doc/models/bank-account-identification.md)

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `bic` | `str` | Optional | The bank's 8- or 11-character BIC or SWIFT code. |
| `iban` | `str` | Required | The international bank account number as defined in the [ISO-13616](https://www.iso.org/standard/81090.html) standard. |

## Example

```python
from adyen.models.bank_account_identification import IbanAccountIdentification1

iban_account_identification_1 = IbanAccountIdentification1(
    iban='iban4',
    bic='bic2',
    mtype='iban'
)
```

