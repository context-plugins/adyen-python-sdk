
# Sweep Schedule

*This model accepts additional fields of type Any.*

## Structure

`SweepSchedule`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `cron_expression` | `str` | Optional | A [cron expression](https://en.wikipedia.org/wiki/Cron#CRON_expression) that is used to set the sweep schedule. The schedule uses the time zone of the balance account.<br>For example, **30 17 * * MON** schedules a sweep every Monday at 17:30.<br><br>The expression must have five values separated by a single space in the following order:<br><br>* Minute: **0-59**<br><br>* Hour: **0-23**<br><br>* Day of the month: **1-31**<br><br>* Month: **1-12** or **JAN-DEC**<br><br>* Day of the week: **0-7** (0 and 7 are Sunday) or **MON-SUN**.<br><br>The following non-standard characters are supported: **&ast;**, **L**, **#**, **W** and **/**. See [crontab guru](https://crontab.guru/) for more examples.<br><br>Required when `type` is **cron**. |
| `mtype` | [`Type6`](../../doc/models/type-6.md) | Required | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.sweep_schedule import SweepSchedule
from adyen.models.type_6 import Type6

sweep_schedule = SweepSchedule(
    mtype=Type6.CRON,
    cron_expression='cronExpression4',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

