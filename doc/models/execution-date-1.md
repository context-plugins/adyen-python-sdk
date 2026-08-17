
# Execution Date 1

Contains information about the date when the transfer will be processed. The execution date must be within 30 days of the current date.

Until the execution date:

- The `status` of the transfer remains as **received**.
- The `reason` of the transfer remains as **pending**.

## Structure

`ExecutionDate1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `date` | `date` | Optional | The date when the transfer will be processed. This date must be:<br><br>* Within 30 days of the current date.<br>* In the [ISO 8601 format](https://www.iso.org/iso-8601-date-and-time-format.html) **YYYY-MM-DD**. For example: 2025-01-31 |
| `timezone` | `str` | Optional | The timezone that applies to the execution date. Use a timezone identifier from the [tz database](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones).<br><br>Example: **America/Los_Angeles**.<br>Default value: **Europe/Amsterdam**. |

## Example

```python
import dateutil.parser

from adyen.models.execution_date_1 import ExecutionDate1

execution_date_1 = ExecutionDate1(
    date=dateutil.parser.parse('2016-03-13').date(),
    timezone='timezone8'
)
```

