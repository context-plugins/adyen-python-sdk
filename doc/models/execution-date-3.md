
# Execution Date 3

The date when the transfer will be processed. This date must be within 30 days of the current date.

Until the `executionDate`:

- The `status` of the transfer remains as **received**.
- The `reason` of the transfer remains as **pending**.

## Structure

`ExecutionDate3`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `date` | `date` | Optional | The date when the transfer will be processed. This date must be:<br><br>* Within 30 days of the current date.<br>* In the [ISO 8601 format](https://www.iso.org/iso-8601-date-and-time-format.html) **YYYY-MM-DD**. For example: 2025-01-31 |
| `timezone` | `str` | Optional | The timezone that applies to the execution date. Use a timezone identifier from the [tz database](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones).<br><br>Example: **America/Los_Angeles**.<br>Default value: **Europe/Amsterdam**. |

## Example

```python
import dateutil.parser

from adyen.models.execution_date_3 import ExecutionDate3

execution_date_3 = ExecutionDate3(
    date=dateutil.parser.parse('2016-03-13').date(),
    timezone='timezone4'
)
```

