
# Afterpay Touch Info

*This model accepts additional fields of type Any.*

## Structure

`AfterpayTouchInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `support_email` | `str` | Optional | Support Email |
| `support_url` | `str` | Required | Support Url |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.afterpay_touch_info import AfterpayTouchInfo

afterpay_touch_info = AfterpayTouchInfo(
    support_url='supportUrl0',
    support_email='supportEmail4',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

