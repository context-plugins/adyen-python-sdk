
# Return Transfer Response

## Structure

`ReturnTransferResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | The unique identifier of the return. |
| `reference` | `str` | Optional | Your internal reference for the return. |
| `status` | [`Status62Enum`](../../doc/models/status-62-enum.md) | Optional | The resulting status of the return.<br><br>Possible values: **Authorised**, **Declined**. |
| `transfer_id` | `str` | Optional | The unique identifier of the original transfer. |

## Example

```python
from adyen.models.return_transfer_response import ReturnTransferResponse
from adyen.models.status_62_enum import Status62Enum

return_transfer_response = ReturnTransferResponse(
    id='id8',
    reference='reference4',
    status=Status62Enum.AUTHORISED,
    transfer_id='transferId6'
)
```

