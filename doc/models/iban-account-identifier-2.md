
# Iban Account Identifier 2

The international bank account number as defined in the ISO-13616 standard.

*This model accepts additional fields of type Any.*

## Structure

`IbanAccountIdentifier2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `bban` | `str` | Required | The Basic Bank Account Number (BBAN) component of the IBAN. |
| `bic` | `str` | Required | BIC of a bank account. |
| `iban` | `str` | Required | The international bank account number as defined in the [ISO-13616](https://www.iso.org/standard/81090.html) standard. This is the national identifier for the bank account, following the country-specific format, and is part of the full IBAN. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.iban_account_identifier_2 import IbanAccountIdentifier2

iban_account_identifier_2 = IbanAccountIdentifier2(
    bban='bban2',
    bic='bic6',
    iban='iban8',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

