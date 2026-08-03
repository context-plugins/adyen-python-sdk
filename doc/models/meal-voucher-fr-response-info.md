
# Meal Voucher Fr Response Info

*This model accepts additional fields of type Any.*

## Structure

`MealVoucherFrResponseInfo`

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

from adyen.models.meal_voucher_fr_response_info import MealVoucherFrResponseInfo

meal_voucher_fr_response_info = MealVoucherFrResponseInfo(
    conecs_id='conecsId4',
    siret='siret0',
    sub_types=[
        'subTypes9',
        'subTypes0',
        'subTypes1'
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

