
# Apple Pay Response Info

## Structure

`ApplePayResponseInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `domains` | `List[str]` | Optional | The list of merchant domains.<br><br>For more information, see [Apple Pay documentation](https://docs.adyen.com/payment-methods/apple-pay/web-drop-in?tab=adyen-certificate-live_1#going-live). |

## Example

```python
from adyen.models.apple_pay_response_info import ApplePayResponseInfo

apple_pay_response_info = ApplePayResponseInfo(
    domains=[
        'domains8',
        'domains9',
        'domains0'
    ]
)
```

