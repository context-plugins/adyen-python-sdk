
# IBAN Account Identifier

## Structure

`IBANAccountIdentifier`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `bban` | `str` | Required | The Basic Bank Account Number (BBAN) component of the IBAN. |
| `bic` | `str` | Required | BIC of a bank account. |
| `iban` | `str` | Required | The international bank account number as defined in the [ISO-13616](https://www.iso.org/standard/81090.html) standard. This is the national identifier for the bank account, following the country-specific format, and is part of the full IBAN. |

## Example

```python
from adyen.models.iban_account_identifier import IBANAccountIdentifier

iban_account_identifier = IBANAccountIdentifier(
    bban='bban6',
    bic='bic4',
    iban='iban6'
)
```

