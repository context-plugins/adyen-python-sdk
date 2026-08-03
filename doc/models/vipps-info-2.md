
# Vipps Info 2

Details to provide if `type` is **vipps**.

*This model accepts additional fields of type Any.*

## Structure

`VippsInfo2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `logo` | `str` | Required | Vipps logo. Format: Base64-encoded string. |
| `subscription_cancel_url` | `str` | Optional | Vipps subscription cancel url (required in case of [recurring payments](https://docs.adyen.com/online-payments/tokenization)) |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.vipps_info_2 import VippsInfo2

vipps_info_2 = VippsInfo2(
    logo='logo8',
    subscription_cancel_url='subscriptionCancelUrl6',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

