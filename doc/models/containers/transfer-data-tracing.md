
# Transfer Data Tracing

## Data Type

`UkFpsTracingData | UsAchTracingData`

## Cases

| Type |
|  --- |
| [`UkFpsTracingData`](../../../doc/models/uk-fps-tracing-data.md) |
| [`UsAchTracingData`](../../../doc/models/us-ach-tracing-data.md) |

## UkFpsTracingData

### Initialization Code

#### Example

```python
value = UkFpsTracingData(
    fpid='fpid0',
    mtype=Type88.UKFPS
)
```

## UsAchTracingData

### Initialization Code

#### Example

```python
value = UsAchTracingData(
    trace_number='traceNumber8',
    mtype=Type89.USACH
)
```

