
# Other Info 3

Additional information for raising a dispute of `type` **other**. Required for disputes of `type` **other**.

**Note:** The **other** dispute `type` is currently in beta testing. Do not create or submit any disputes for this dispute `type` at this time.

*This model accepts additional fields of type Any.*

## Structure

`OtherInfo3`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `description_of_issue` | `str` | Required | Your description of the issue for raising a dispute of `type` **other**.<br><br>**Constraints**: *Minimum Length*: `0`, *Maximum Length*: `2500` |
| `sub_type` | [`SubType11`](../../doc/models/sub-type-11.md) | Required | - |
| `what_was_purchased` | [`ProductType1`](../../doc/models/product-type-1.md) | Required | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.other_info_3 import OtherInfo3
from adyen.models.product_type_1 import ProductType1
from adyen.models.sub_type_11 import SubType11

other_info_3 = OtherInfo3(
    description_of_issue='descriptionOfIssue6',
    sub_type=SubType11.CANCELLEDRECURRING,
    what_was_purchased=ProductType1.GOODS,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

