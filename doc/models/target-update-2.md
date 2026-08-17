
# Target Update 2

The type and ID of the resource about whose balance changes you want to be notified.

## Structure

`TargetUpdate2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | The unique identifier of the `target.type`. This can be the ID of your:<br><br>* balance platform<br>* account holder<br>* account holder's balance account<br><br>**Constraints**: *Minimum Length*: `1` |
| `mtype` | [`Type181Enum`](../../doc/models/type-181-enum.md) | Optional | The resource for which you want to receive notifications. Possible values:<br><br>* **balancePlatform**: receive notifications about balance changes in your entire balance platform.<br><br>* **accountHolder**: receive notifications about balance changes of a specific user.<br><br>* **balanceAccount**: receive notifications about balance changes in a specific balance account. |

## Example

```python
from adyen.models.target_update_2 import TargetUpdate2
from adyen.models.type_181_enum import Type181Enum

target_update_2 = TargetUpdate2(
    id='id8',
    mtype=Type181Enum.BALANCEPLATFORM
)
```

