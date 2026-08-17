
# Modification 2

The payment modification. Only applicable for [returned internal transfers](https://docs.adyen.com/platforms/internal-fund-transfers/internal-transfer-webhooks/#returned-internal-transfer).

## Structure

`Modification2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `direction` | `str` | Optional | The direction of the money movement. |
| `id` | `str` | Optional | Our reference for the modification. |
| `reference` | `str` | Optional | Your reference for the modification, used internally within your platform. |
| `status` | [`Status24Enum`](../../doc/models/status-24-enum.md) | Optional | The status of the transfer event. |
| `mtype` | `str` | Optional | The type of transfer modification. |

## Example

```python
from adyen.models.modification_2 import Modification2
from adyen.models.status_24_enum import Status24Enum

modification_2 = Modification2(
    direction='direction8',
    id='id2',
    reference='reference2',
    status=Status24Enum.MERCHANTPAYIN,
    mtype='type8'
)
```

