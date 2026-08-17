
# Release Update Details

## Structure

`ReleaseUpdateDetails`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | [`Type61Enum`](../../doc/models/type-61-enum.md) | Optional | Type of terminal action: Update Release.<br><br>**Default**: `"ReleaseUpdate"` |
| `update_at_first_maintenance_call` | `bool` | Optional | Boolean flag that tells if the terminal should update at the first next maintenance call. If false, terminal will update on its configured reboot time. |

## Example

```python
from adyen.models.release_update_details import ReleaseUpdateDetails
from adyen.models.type_61_enum import Type61Enum

release_update_details = ReleaseUpdateDetails(
    mtype=Type61Enum.RELEASEUPDATE,
    update_at_first_maintenance_call=False
)
```

