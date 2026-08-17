
# Iban Account Identification

## Structure

`IbanAccountIdentification`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `bic` | `str` | Optional | The bank's 8- or 11-character BIC or SWIFT code. |
| `iban` | `str` | Required | The international bank account number as defined in the [ISO-13616](https://www.iso.org/standard/81090.html) standard. |
| `mtype` | `str` | Required, Constant | **iban**<br><br>**Value**: `"iban"` |

## Example

```python
from adyen.models.iban_account_identification import IbanAccountIdentification

iban_account_identification = IbanAccountIdentification(
    iban='iban8',
    bic='bic6'
)
```

