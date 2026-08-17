
# Apple Pay Info

## Structure

`ApplePayInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `domains` | `List[str]` | Required | The list of merchant domains. Maximum: 99 domains per request.<br><br>For more information, see [Apple Pay documentation](https://docs.adyen.com/payment-methods/apple-pay/web-drop-in?tab=adyen-certificate-live_1#going-live). |

## Example

```python
from adyen.models.apple_pay_info import ApplePayInfo

apple_pay_info = ApplePayInfo(
    domains=[
        'domains0',
        'domains1'
    ]
)
```

