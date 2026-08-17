
# Update Network Token Request

## Structure

`UpdateNetworkTokenRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `status` | [`Status16Enum`](../../doc/models/status-16-enum.md) | Optional | The new status of the network token. Possible values: **active**, **suspended**, **closed**. The **closed** status is final and cannot be changed. |

## Example

```python
from adyen.models.status_16_enum import Status16Enum
from adyen.models.update_network_token_request import UpdateNetworkTokenRequest

update_network_token_request = UpdateNetworkTokenRequest(
    status=Status16Enum.CLOSED
)
```

