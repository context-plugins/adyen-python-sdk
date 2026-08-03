
# Amex Info 1

Details to provide if `type` is **amex**.
For merchants operating in Australia, New Zealand & Canada, JCB and American Express are automatically requested together.

*This model accepts additional fields of type Any.*

## Structure

`AmexInfo1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mid_number` | `str` | Optional | Merchant ID (MID) number. Format: 10 numeric characters.<br>You must provide this field when you request `gatewayContract` or `paymentDesignatorContract` service levels.<br><br>**Constraints**: *Maximum Length*: `10` |
| `reuse_mid_number` | `bool` | Optional | Indicates whether the Amex Merchant ID is reused from a previously setup Amex payment method.<br>This is only applicable for `gatewayContract` and `paymentDesignatorContract` service levels.<br>The default value is **false**.<br><br>**Default**: `False` |
| `service_level` | [`ServiceLevel`](../../doc/models/service-level.md) | Required | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.amex_info_1 import AmexInfo1
from adyen.models.service_level import ServiceLevel

amex_info_1 = AmexInfo1(
    service_level=ServiceLevel.NOCONTRACT,
    mid_number='midNumber6',
    reuse_mid_number=False,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

