
# Us Local Account Identification

*This model accepts additional fields of type Any.*

## Structure

`UsLocalAccountIdentification`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_number` | `str` | Required | The bank account number, without separators or whitespace.<br><br>**Constraints**: *Minimum Length*: `2`, *Maximum Length*: `18` |
| `account_type` | [`AccountType`](../../doc/models/account-type.md) | Optional | - |
| `routing_number` | `str` | Required | The 9-digit [routing number](https://en.wikipedia.org/wiki/ABA_routing_transit_number), without separators or whitespace.<br><br>**Constraints**: *Minimum Length*: `9`, *Maximum Length*: `9` |
| `mtype` | [`Type283`](../../doc/models/type-283.md) | Required | **usLocal** |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.account_type import AccountType
from adyen.models.type_283 import Type283
from adyen.models.us_local_account_identification import UsLocalAccountIdentification

us_local_account_identification = UsLocalAccountIdentification(
    account_number='accountNumber6',
    routing_number='routingNumber8',
    mtype=Type283.USLOCAL,
    account_type=AccountType.CHECKING,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

