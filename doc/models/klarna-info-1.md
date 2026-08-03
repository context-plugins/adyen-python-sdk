
# Klarna Info 1

Details to provide if `type` is **klarna** or its variant.

You can use the following payment method `type` values for Klarna:

* **klarna**: Klarna Pay Later
* **klarna_account**: Klarna Pay over time
* **klarna_paynow**: Klarna Pay now
* **klarna_b2b**: [Billie via Klarna](https://docs.adyen.com/payment-methods/klarna/billie)

*This model accepts additional fields of type Any.*

## Structure

`KlarnaInfo1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `auto_capture` | `bool` | Optional | Indicates the status of [Automatic capture](https://docs.adyen.com/online-payments/capture#automatic-capture). Default value: **false**. |
| `dispute_email` | `str` | Required | The email address for disputes. |
| `region` | [`Region`](../../doc/models/region.md) | Required | **Constraints**: *Minimum Length*: `2`, *Maximum Length*: `2` |
| `support_email` | `str` | Required | The email address of merchant support. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.klarna_info_1 import KlarnaInfo1
from adyen.models.region import Region

klarna_info_1 = KlarnaInfo1(
    dispute_email='disputeEmail0',
    region=Region.CH,
    support_email='supportEmail4',
    auto_capture=False,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

