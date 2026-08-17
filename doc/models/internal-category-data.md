
# Internal Category Data

## Structure

`InternalCategoryData`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `modification_merchant_reference` | `str` | Optional | The capture's merchant reference included in the transfer. |
| `modification_psp_reference` | `str` | Optional | The capture reference included in the transfer. |
| `mtype` | [`Type411Enum`](../../doc/models/type-411-enum.md) | Optional | **internal**<br><br>**Default**: `"internal"` |

## Example

```python
from adyen.models.internal_category_data import InternalCategoryData
from adyen.models.type_411_enum import Type411Enum

internal_category_data = InternalCategoryData(
    modification_merchant_reference='modificationMerchantReference4',
    modification_psp_reference='modificationPspReference2',
    mtype=Type411Enum.INTERNAL
)
```

