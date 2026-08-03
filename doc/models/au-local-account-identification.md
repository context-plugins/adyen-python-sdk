
# Au Local Account Identification

*This model accepts additional fields of type Any.*

## Structure

`AuLocalAccountIdentification`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_number` | `str` | Required | The bank account number, without separators or whitespace.<br><br>**Constraints**: *Minimum Length*: `5`, *Maximum Length*: `9` |
| `bsb_code` | `str` | Required | The 6-digit [Bank State Branch (BSB) code](https://en.wikipedia.org/wiki/Bank_state_branch), without separators or whitespace.<br><br>**Constraints**: *Minimum Length*: `6`, *Maximum Length*: `6` |
| `mtype` | [`Type413`](../../doc/models/type-413.md) | Required | **auLocal** |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.au_local_account_identification import AuLocalAccountIdentification
from adyen.models.type_413 import Type413

au_local_account_identification = AuLocalAccountIdentification(
    account_number='accountNumber2',
    bsb_code='bsbCode4',
    mtype=Type413.AULOCAL,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

