
# Meal Voucher Fr Response Info 1

**mealVoucher_FR** details

*This model accepts additional fields of type Any.*

## Structure

`MealVoucherFrResponseInfo1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `conecs_id` | `str` | Optional | Meal Voucher conecsId. |
| `siret` | `str` | Optional | Meal Voucher siret. |
| `sub_types` | `List[str]` | Optional | The list of additional payment methods. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.meal_voucher_fr_response_info_1 import MealVoucherFrResponseInfo1

meal_voucher_fr_response_info_1 = MealVoucherFrResponseInfo1(
    conecs_id='conecsId4',
    siret='siret0',
    sub_types=[
        'subTypes9'
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

