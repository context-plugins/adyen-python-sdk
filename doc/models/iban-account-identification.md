
# Iban Account Identification

*This model accepts additional fields of type Any.*

## Structure

`IbanAccountIdentification`

## Inherits From

[`AccountIdentification`](../../doc/models/account-identification.md)

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `iban` | `str` | Required | The IBAN of the bank account.<br><br>**Constraints**: *Minimum Length*: `1` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.account_identification import IbanAccountIdentification

iban_account_identification = IbanAccountIdentification(
    iban='NL00AAAA0000000000',
    mtype='iban',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

