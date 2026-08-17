
# UK Fps Tracing Data

## Structure

`UKFpsTracingData`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `fpid` | `str` | Required | The FPS trace number. This is a unique identifier assigned to transfers processed by [FPS](https://www.bankofengland.co.uk/payment-systems/services/faster-payments-service). |
| `mtype` | `str` | Required, Constant | **ukFps**<br><br>**Value**: `"ukFps"` |

## Example

```python
from adyen.models.uk_fps_tracing_data import UKFpsTracingData

uk_fps_tracing_data = UKFpsTracingData(
    fpid='fpid0'
)
```

