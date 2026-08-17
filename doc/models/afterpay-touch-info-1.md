
# Afterpay Touch Info 1

Details to provide if `type` is **afterpaytouch**.

## Structure

`AfterpayTouchInfo1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `support_email` | `str` | Optional | Support Email |
| `support_url` | `str` | Required | Support Url |

## Example

```python
from adyen.models.afterpay_touch_info_1 import AfterpayTouchInfo1

afterpay_touch_info_1 = AfterpayTouchInfo1(
    support_url='supportUrl6',
    support_email='supportEmail0'
)
```

