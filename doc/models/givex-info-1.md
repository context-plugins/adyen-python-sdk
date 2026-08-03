
# Givex Info 1

Details to provide if `type` is **givex**.

*This model accepts additional fields of type Any.*

## Structure

`GivexInfo1`

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

from adyen.models.givex_info_1 import GivexInfo1
from adyen.models.shopper_interaction import ShopperInteraction

givex_info_1 = GivexInfo1(
    currency_code='currencyCode2',
    password='password6',
    payment_flow=ShopperInteraction.ECOMMERCE,
    username='username8',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

