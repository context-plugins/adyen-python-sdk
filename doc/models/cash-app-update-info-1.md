
# Cash App Update Info 1

Details to provide if `type` is **cashapp**.

## Structure

`CashAppUpdateInfo1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `logo_url` | `str` | Optional | The URL of the logo image shown in Cash App checkout next to payments. |
| `merchant_name` | `str` | Optional | The merchant display name shown in Cash App checkout. |

## Example

```python
from adyen.models.cash_app_update_info_1 import CashAppUpdateInfo1

cash_app_update_info_1 = CashAppUpdateInfo1(
    logo_url='logoUrl8',
    merchant_name='merchantName8'
)
```

