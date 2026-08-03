
# Iban Account Identifier

*This model accepts additional fields of type Any.*

## Structure

`IbanAccountIdentifier`

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

from adyen.models.iban_account_identifier import IbanAccountIdentifier

iban_account_identifier = IbanAccountIdentifier(
    bban='bban6',
    bic='bic4',
    iban='iban6',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

