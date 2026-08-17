
# Timeouts

## Structure

`Timeouts`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `from_active_to_sleep` | `int` | Optional | Indicates the number of seconds of inactivity after which the terminal display goes into sleep mode. |

## Example

```python
from adyen.models.timeouts import Timeouts

timeouts = Timeouts(
    from_active_to_sleep=94
)
```

