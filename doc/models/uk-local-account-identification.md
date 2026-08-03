
# Uk Local Account Identification

*This model accepts additional fields of type Any.*

## Structure

`UkLocalAccountIdentification`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_number` | `str` | Required | The 8-digit bank account number, without separators or whitespace.<br><br>**Constraints**: *Minimum Length*: `8`, *Maximum Length*: `8` |
| `sort_code` | `str` | Required | The 6-digit [sort code](https://en.wikipedia.org/wiki/Sort_code), without separators or whitespace.<br><br>**Constraints**: *Minimum Length*: `6`, *Maximum Length*: `6` |
| `mtype` | [`Type273`](../../doc/models/type-273.md) | Required | **ukLocal** |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.type_273 import Type273
from adyen.models.uk_local_account_identification import UkLocalAccountIdentification

uk_local_account_identification = UkLocalAccountIdentification(
    account_number='accountNumber6',
    sort_code='sortCode4',
    mtype=Type273.UKLOCAL,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

