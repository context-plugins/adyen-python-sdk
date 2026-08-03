
# Transaction Rule Interval

*This model accepts additional fields of type Any.*

## Structure

`TransactionRuleInterval`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `day_of_month` | `int` | Optional | The day of month, used when the `duration.unit` is **months**. If not provided, by default, this is set to **1**, the first day of the month. |
| `day_of_week` | [`DayOfWeek`](../../doc/models/day-of-week.md) | Optional | - |
| `duration` | [`Duration`](../../doc/models/duration.md) | Optional | - |
| `time_of_day` | `str` | Optional | The time of day, in **hh:mm:ss** format, used when the `duration.unit` is **hours**. If not provided, by default, this is set to **00:00:00**. |
| `time_zone` | `str` | Optional | The [time zone](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones). For example, **Europe/Amsterdam**. By default, this is set to **UTC**. |
| `mtype` | [`Type13`](../../doc/models/type-13.md) | Required | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.day_of_week import DayOfWeek
from adyen.models.duration import Duration
from adyen.models.transaction_rule_interval import TransactionRuleInterval
from adyen.models.type_13 import Type13
from adyen.models.unit import Unit

transaction_rule_interval = TransactionRuleInterval(
    mtype=Type13.LIFETIME,
    day_of_month=26,
    day_of_week=DayOfWeek.SUNDAY,
    duration=Duration(
        unit=Unit.WEEKS,
        value=176,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    time_of_day='timeOfDay2',
    time_zone='timeZone4',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

