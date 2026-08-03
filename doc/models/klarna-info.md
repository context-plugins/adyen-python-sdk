
# Klarna Info

*This model accepts additional fields of type Any.*

## Structure

`KlarnaInfo`

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

from adyen.models.klarna_info import KlarnaInfo
from adyen.models.region import Region

klarna_info = KlarnaInfo(
    dispute_email='disputeEmail4',
    region=Region.NA,
    support_email='supportEmail8',
    auto_capture=False,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

