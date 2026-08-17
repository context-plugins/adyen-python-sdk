
# IBAN Account Identifier 2

The international bank account number as defined in the ISO-13616 standard.

## Structure

`IBANAccountIdentifier2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `bban` | `str` | Required | The Basic Bank Account Number (BBAN) component of the IBAN. |
| `bic` | `str` | Required | BIC of a bank account. |
| `iban` | `str` | Required | The international bank account number as defined in the [ISO-13616](https://www.iso.org/standard/81090.html) standard. This is the national identifier for the bank account, following the country-specific format, and is part of the full IBAN. |

## Example

```python
from adyen.models.iban_account_identifier_2 import IBANAccountIdentifier2

iban_account_identifier_2 = IBANAccountIdentifier2(
    bban='bban2',
    bic='bic6',
    iban='iban8'
)
```

