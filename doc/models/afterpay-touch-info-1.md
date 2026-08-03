
# Afterpay Touch Info 1

Details to provide if `type` is **afterpaytouch**.

*This model accepts additional fields of type Any.*

## Structure

`AfterpayTouchInfo1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `support_email` | `str` | Optional | Support Email |
| `support_url` | `str` | Required | Support Url |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.afterpay_touch_info_1 import AfterpayTouchInfo1

afterpay_touch_info_1 = AfterpayTouchInfo1(
    support_url='supportUrl6',
    support_email='supportEmail0',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

