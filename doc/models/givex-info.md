
# Givex Info

*This model accepts additional fields of type Any.*

## Structure

`GivexInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `currency_code` | `str` | Required | The three-character ISO currency code, such as **EUR**. |
| `password` | `str` | Required | The password provided by the acquirer. |
| `payment_flow` | [`ShopperInteraction`](../../doc/models/shopper-interaction.md) | Required | - |
| `username` | `str` | Required | The username provided by the acquirer. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.givex_info import GivexInfo
from adyen.models.shopper_interaction import ShopperInteraction

givex_info = GivexInfo(
    currency_code='currencyCode0',
    password='password4',
    payment_flow=ShopperInteraction.ECOMMERCE,
    username='username0',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

