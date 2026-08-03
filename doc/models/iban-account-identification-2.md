
# Iban Account Identification 2

*This model accepts additional fields of type Any.*

## Structure

`IbanAccountIdentification2`

## Inherits From

[`BankAccountIdentification`](../../doc/models/bank-account-identification.md)

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `bic` | `str` | Optional | The bank's 8- or 11-character BIC or SWIFT code. |
| `iban` | `str` | Required | The international bank account number as defined in the [ISO-13616](https://www.iso.org/standard/81090.html) standard. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.bank_account_identification import IbanAccountIdentification2

iban_account_identification_2 = IbanAccountIdentification2(
    iban='iban8',
    bic='bic6',
    mtype='iban',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

