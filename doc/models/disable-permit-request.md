
# Disable Permit Request

## Structure

`DisablePermitRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `merchant_account` | `str` | Required | The merchant account identifier, with which you want to process the transaction. |
| `token` | `str` | Required | The permit token to disable. |

## Example

```python
from adyen.models.disable_permit_request import DisablePermitRequest

disable_permit_request = DisablePermitRequest(
    merchant_account='merchantAccount8',
    token='token0'
)
```

