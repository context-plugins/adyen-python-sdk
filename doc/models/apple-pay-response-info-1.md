
# Apple Pay Response Info 1

**applepay** details

*This model accepts additional fields of type Any.*

## Structure

`ApplePayResponseInfo1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `domains` | `List[str]` | Optional | The list of merchant domains.<br><br>For more information, see [Apple Pay documentation](https://docs.adyen.com/payment-methods/apple-pay/web-drop-in?tab=adyen-certificate-live_1#going-live). |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.apple_pay_response_info_1 import ApplePayResponseInfo1

apple_pay_response_info_1 = ApplePayResponseInfo1(
    domains=[
        'domains6',
        'domains7',
        'domains8'
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

