
# Afterpay Touch Info

## Structure

`AfterpayTouchInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `support_email` | `str` | Optional | Support Email |
| `support_url` | `str` | Required | Support Url |

## Example

```python
from adyen.models.afterpay_touch_info import AfterpayTouchInfo

afterpay_touch_info = AfterpayTouchInfo(
    support_url='supportUrl0',
    support_email='supportEmail4'
)
```

