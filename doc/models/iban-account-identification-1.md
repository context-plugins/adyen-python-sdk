
# Iban Account Identification 1

*This model accepts additional fields of type Any.*

## Structure

`IbanAccountIdentification1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `bic` | `str` | Optional | The bank's 8- or 11-character BIC or SWIFT code. |
| `iban` | `str` | Required | The international bank account number as defined in the [ISO-13616](https://www.iso.org/standard/81090.html) standard. |
| `mtype` | [`Type203`](../../doc/models/type-203.md) | Required | **iban** |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.iban_account_identification_1 import IbanAccountIdentification1
from adyen.models.type_203 import Type203

iban_account_identification_1 = IbanAccountIdentification1(
    iban='iban4',
    mtype=Type203.IBAN,
    bic='bic2',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

