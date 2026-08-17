
# Meal Voucher FR Response Info 1

**mealVoucher_FR** details

## Structure

`MealVoucherFRResponseInfo1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `conecs_id` | `str` | Optional | Meal Voucher conecsId. |
| `siret` | `str` | Optional | Meal Voucher siret. |
| `sub_types` | `List[str]` | Optional | The list of additional payment methods. |

## Example

```python
from adyen.models.meal_voucher_fr_response_info_1 import MealVoucherFRResponseInfo1

meal_voucher_fr_response_info_1 = MealVoucherFRResponseInfo1(
    conecs_id='conecsId4',
    siret='siret0',
    sub_types=[
        'subTypes9'
    ]
)
```

