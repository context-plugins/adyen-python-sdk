
# Apple Pay Response Info 1

**applepay** details

## Structure

`ApplePayResponseInfo1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `domains` | `List[str]` | Optional | The list of merchant domains.<br><br>For more information, see [Apple Pay documentation](https://docs.adyen.com/payment-methods/apple-pay/web-drop-in?tab=adyen-certificate-live_1#going-live). |

## Example

```python
from adyen.models.apple_pay_response_info_1 import ApplePayResponseInfo1

apple_pay_response_info_1 = ApplePayResponseInfo1(
    domains=[
        'domains6',
        'domains7',
        'domains8'
    ]
)
```

