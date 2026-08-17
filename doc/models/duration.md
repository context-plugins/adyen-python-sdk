
# Duration

## Structure

`Duration`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `unit` | [`UnitEnum`](../../doc/models/unit-enum.md) | Optional | The unit of time. You can only use **minutes** and **hours** if the `interval.type` is **sliding**.<br><br>Possible values: **minutes**, **hours**, **days**, **weeks**, or **months** |
| `value` | `int` | Optional | The length of time by the unit. For example, 5 days.<br><br>The maximum duration is 90 days or an equivalent in other units. For example, 3 months. |

## Example

```python
from adyen.models.duration import Duration
from adyen.models.unit_enum import UnitEnum

duration = Duration(
    unit=UnitEnum.WEEKS,
    value=176
)
```

