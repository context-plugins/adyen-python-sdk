
# Counterparty

*This model accepts additional fields of type Any.*

## Structure

`Counterparty`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_holder` | [`AccountHolder`](../../doc/models/account-holder.md) | Required | - |
| `account_identification` | [`AccountIdentification1`](../../doc/models/account-identification-1.md) | Required | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.account_holder import AccountHolder
from adyen.models.account_identification_1 import AccountIdentification1
from adyen.models.counterparty import Counterparty

counterparty = Counterparty(
    account_holder=AccountHolder(
        full_name='John Doe',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    account_identification=AccountIdentification1(
        mtype='AccountIdentification1',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

