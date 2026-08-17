
# Update Payout Settings Request

## Structure

`UpdatePayoutSettingsRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `enabled` | `bool` | Optional | Indicates if payouts to this bank account are enabled. Default: **true**.<br><br>To receive payouts into this bank account, both `enabled` and `allowed` must be **true**. |

## Example

```python
from adyen.models.update_payout_settings_request import UpdatePayoutSettingsRequest

update_payout_settings_request = UpdatePayoutSettingsRequest(
    enabled=False
)
```

