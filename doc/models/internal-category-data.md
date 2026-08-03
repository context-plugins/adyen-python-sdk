
# Internal Category Data

*This model accepts additional fields of type Any.*

## Structure

`InternalCategoryData`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `modification_merchant_reference` | `str` | Optional | The capture's merchant reference included in the transfer. |
| `modification_psp_reference` | `str` | Optional | The capture reference included in the transfer. |
| `mtype` | [`Type410`](../../doc/models/type-410.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.internal_category_data import InternalCategoryData
from adyen.models.type_410 import Type410

internal_category_data = InternalCategoryData(
    modification_merchant_reference='modificationMerchantReference4',
    modification_psp_reference='modificationPspReference2',
    mtype=Type410.INTERNAL,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

