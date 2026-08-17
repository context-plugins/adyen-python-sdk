
# Iban Account Identification 2

## Structure

`IbanAccountIdentification2`

## Inherits From

[`AccountIdentification`](../../doc/models/account-identification.md)

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `iban` | `str` | Required | The IBAN of the bank account.<br><br>**Constraints**: *Minimum Length*: `1` |

## Example

```python
from adyen.models.account_identification import IbanAccountIdentification2

iban_account_identification_2 = IbanAccountIdentification2(
    iban='NL00AAAA0000000000',
    mtype='iban'
)
```

