
# US Local Account Identification

## Structure

`USLocalAccountIdentification`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_number` | `str` | Required | The bank account number, without separators or whitespace.<br><br>**Constraints**: *Minimum Length*: `2`, *Maximum Length*: `18` |
| `account_type` | [`AccountType2Enum`](../../doc/models/account-type-2-enum.md) | Optional | The bank account type.<br><br>Possible values: **checking** or **savings**. Defaults to **checking**.<br><br>**Default**: `"checking"` |
| `routing_number` | `str` | Required | The 9-digit [routing number](https://en.wikipedia.org/wiki/ABA_routing_transit_number), without separators or whitespace.<br><br>**Constraints**: *Minimum Length*: `9`, *Maximum Length*: `9` |
| `mtype` | `str` | Required, Constant | **usLocal**<br><br>**Value**: `"usLocal"` |

## Example

```python
from adyen.models.account_type_2_enum import AccountType2Enum
from adyen.models.us_local_account_identification import USLocalAccountIdentification

us_local_account_identification = USLocalAccountIdentification(
    account_number='accountNumber6',
    routing_number='routingNumber8',
    account_type=AccountType2Enum.CHECKING
)
```

