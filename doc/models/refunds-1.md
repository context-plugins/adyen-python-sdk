
# Refunds 1

Settings for refunds.

*This model accepts additional fields of type Any.*

## Structure

`Refunds1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `referenced` | [`Referenced`](../../doc/models/referenced.md) | Optional | - |
| `unreferenced` | [`Unreferenced`](../../doc/models/unreferenced.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.referenced import Referenced
from adyen.models.refunds_1 import Refunds1
from adyen.models.unreferenced import Unreferenced

refunds_1 = Refunds1(
    referenced=Referenced(
        enable_standalone_refunds=False,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    unreferenced=Unreferenced(
        enable_unreferenced_refunds=False,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

