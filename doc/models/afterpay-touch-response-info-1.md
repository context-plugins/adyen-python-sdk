
# Afterpay Touch Response Info 1

**afterpaytouch** details

*This model accepts additional fields of type Any.*

## Structure

`AfterpayTouchResponseInfo1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `support_email` | `str` | Optional | Support Email |
| `support_url` | `str` | Optional | Support Url |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.afterpay_touch_response_info_1 import AfterpayTouchResponseInfo1

afterpay_touch_response_info_1 = AfterpayTouchResponseInfo1(
    support_email='supportEmail2',
    support_url='supportUrl8',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

