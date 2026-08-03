
# Klarna Response Info 1

**klarna** or its variant details

*This model accepts additional fields of type Any.*

## Structure

`KlarnaResponseInfo1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `auto_capture` | `bool` | Optional | Indicates the status of [Automatic capture](https://docs.adyen.com/online-payments/capture#automatic-capture). |
| `dispute_email` | `str` | Optional | The email address for disputes. |
| `region` | [`Region1`](../../doc/models/region-1.md) | Optional | - |
| `support_email` | `str` | Optional | The email address of merchant support. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.klarna_response_info_1 import KlarnaResponseInfo1
from adyen.models.region_1 import Region1

klarna_response_info_1 = KlarnaResponseInfo1(
    auto_capture=False,
    dispute_email='disputeEmail8',
    region=Region1.EU,
    support_email='supportEmail2',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

