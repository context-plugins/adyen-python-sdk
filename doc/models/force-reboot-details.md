
# Force Reboot Details

## Structure

`ForceRebootDetails`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | [`Type210Enum`](../../doc/models/type-210-enum.md) | Optional | The type of terminal action. The value **ForceReboot** triggers an immediate reboot of the specified terminal(s).<br><br>**Default**: `"ForceReboot"` |

## Example

```python
from adyen.models.force_reboot_details import ForceRebootDetails
from adyen.models.type_210_enum import Type210Enum

force_reboot_details = ForceRebootDetails(
    mtype=Type210Enum.FORCEREBOOT
)
```

