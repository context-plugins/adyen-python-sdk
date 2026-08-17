
# US Ach Tracing Data

## Structure

`USAchTracingData`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `trace_number` | `str` | Required | The ACH trace number. This is a unique 15-digit identifier assigned to transfers processed by [ACH](https://fiscal.treasury.gov/payments-from-government/automated-clearing-house-ach). |
| `mtype` | `str` | Required, Constant | **usAch**<br><br>**Value**: `"usAch"` |

## Example

```python
from adyen.models.us_ach_tracing_data import USAchTracingData

us_ach_tracing_data = USAchTracingData(
    trace_number='traceNumber4'
)
```

