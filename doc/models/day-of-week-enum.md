
# Day of Week Enum

The day of week, used when the `duration.unit` is **weeks**. If not provided, by default, this is set to **monday**.

Possible values: **sunday**, **monday**, **tuesday**, **wednesday**, **thursday**, **friday**.

## Enumeration

`DayOfWeekEnum`

## Fields

| Name |
|  --- |
| `FRIDAY` |
| `MONDAY` |
| `SATURDAY` |
| `SUNDAY` |
| `THURSDAY` |
| `TUESDAY` |
| `WEDNESDAY` |

## Example

```python
from adyen.models.day_of_week_enum import DayOfWeekEnum

day_of_week = DayOfWeekEnum.WEDNESDAY
```

