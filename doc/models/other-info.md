
# Other Info

## Structure

`OtherInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `description_of_issue` | `str` | Required | Your description of the issue for raising a dispute of `type` **other**.<br><br>**Constraints**: *Minimum Length*: `0`, *Maximum Length*: `2500` |
| `sub_type` | [`SubType11Enum`](../../doc/models/sub-type-11-enum.md) | Required | The specific category of **other** dispute that you are raising.<br><br>Possible values: **atmDispute**, **cancelledGoodsServices**, **cancelledRecurring**, **counterfeit**, **creditNotProcessed**, **notAsDescribed**. |
| `what_was_purchased` | [`ProductType11Enum`](../../doc/models/product-type-11-enum.md) | Required | The type of product that you purchased.<br><br>Possible values: **goods**, **services**. |

## Example

```python
from adyen.models.other_info import OtherInfo
from adyen.models.product_type_11_enum import ProductType11Enum
from adyen.models.sub_type_11_enum import SubType11Enum

other_info = OtherInfo(
    description_of_issue='descriptionOfIssue4',
    sub_type=SubType11Enum.COUNTERFEIT,
    what_was_purchased=ProductType11Enum.GOODS
)
```

