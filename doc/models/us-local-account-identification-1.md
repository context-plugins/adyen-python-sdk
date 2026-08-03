
# Us Local Account Identification 1

*This model accepts additional fields of type Any.*

## Structure

`UsLocalAccountIdentification1`

## Inherits From

[`BankAccountIdentification`](../../doc/models/bank-account-identification.md)

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_number` | `str` | Required | The bank account number, without separators or whitespace.<br><br>**Constraints**: *Minimum Length*: `2`, *Maximum Length*: `18` |
| `account_type` | [`AccountType`](../../doc/models/account-type.md) | Optional | - |
| `routing_number` | `str` | Required | The 9-digit [routing number](https://en.wikipedia.org/wiki/ABA_routing_transit_number), without separators or whitespace.<br><br>**Constraints**: *Minimum Length*: `9`, *Maximum Length*: `9` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.account_type import AccountType
from adyen.models.bank_account_identification import UsLocalAccountIdentification1

us_local_account_identification_1 = UsLocalAccountIdentification1(
    account_number='accountNumber6',
    routing_number='routingNumber0',
    account_type=AccountType.CHECKING,
    mtype='usLocal',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

