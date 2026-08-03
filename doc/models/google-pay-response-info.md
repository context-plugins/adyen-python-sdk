
# Google Pay Response Info

*This model accepts additional fields of type Any.*

## Structure

`GooglePayResponseInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `merchant_id` | `str` | Optional | Google Pay [Merchant ID] |
| `reuse_merchant_id` | `bool` | Optional | Indicates whether the Google Pay Merchant ID is used for several merchant accounts. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.google_pay_response_info import GooglePayResponseInfo

google_pay_response_info = GooglePayResponseInfo(
    merchant_id='merchantId0',
    reuse_merchant_id=False,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

