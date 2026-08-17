
# Pin Change Response

## Structure

`PinChangeResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `status` | [`Status13Enum`](../../doc/models/status-13-enum.md) | Required | The status of the request for PIN change.<br><br>Possible values: **completed**, **pending**, **unavailable**. |

## Example

```python
from adyen.models.pin_change_response import PinChangeResponse
from adyen.models.status_13_enum import Status13Enum

pin_change_response = PinChangeResponse(
    status=Status13Enum.UNAVAILABLE
)
```

