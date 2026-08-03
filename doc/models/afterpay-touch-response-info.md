
# Afterpay Touch Response Info

*This model accepts additional fields of type Any.*

## Structure

`AfterpayTouchResponseInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `support_email` | `str` | Optional | Support Email |
| `support_url` | `str` | Optional | Support Url |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.afterpay_touch_response_info import AfterpayTouchResponseInfo

afterpay_touch_response_info = AfterpayTouchResponseInfo(
    support_email='supportEmail4',
    support_url='supportUrl0',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

