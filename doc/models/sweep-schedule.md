
# Sweep Schedule

## Structure

`SweepSchedule`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `cron_expression` | `str` | Optional | A [cron expression](https://en.wikipedia.org/wiki/Cron#CRON_expression) that is used to set the sweep schedule. The schedule uses the time zone of the balance account.<br>For example, **30 17 * * MON** schedules a sweep every Monday at 17:30.<br><br>The expression must have five values separated by a single space in the following order:<br><br>* Minute: **0-59**<br><br>* Hour: **0-23**<br><br>* Day of the month: **1-31**<br><br>* Month: **1-12** or **JAN-DEC**<br><br>* Day of the week: **0-7** (0 and 7 are Sunday) or **MON-SUN**.<br><br>The following non-standard characters are supported: **&ast;**, **L**, **#**, **W** and **/**. See [crontab guru](https://crontab.guru/) for more examples.<br><br>Required when `type` is **cron**. |
| `mtype` | [`Type62Enum`](../../doc/models/type-62-enum.md) | Required | The schedule type.<br><br>Possible values:<br><br>* **cron**: push out funds based on a `cronExpression`.<br><br>* **daily**: push out funds daily at 07:00 AM CET.<br><br>* **weekly**: push out funds every Monday at 07:00 AM CET.<br><br>* **monthly**: push out funds every first of the month at 07:00 AM CET.<br><br>* **balance**: execute the sweep instantly if the `triggerAmount` is reached. |

## Example

```python
from adyen.models.sweep_schedule import SweepSchedule
from adyen.models.type_62_enum import Type62Enum

sweep_schedule = SweepSchedule(
    mtype=Type62Enum.CRON,
    cron_expression='cronExpression4'
)
```

