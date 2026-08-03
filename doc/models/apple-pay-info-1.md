
# Apple Pay Info 1

Details to provide if `type` is **applepay**.

*This model accepts additional fields of type Any.*

## Structure

`ApplePayInfo1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `domains` | `List[str]` | Required | The list of merchant domains. Maximum: 99 domains per request.<br><br>For more information, see [Apple Pay documentation](https://docs.adyen.com/payment-methods/apple-pay/web-drop-in?tab=adyen-certificate-live_1#going-live). |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.apple_pay_info_1 import ApplePayInfo1

apple_pay_info_1 = ApplePayInfo1(
    domains=[
        'domains6',
        'domains7'
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

