
# Meal Voucher FR Response Info

## Structure

`MealVoucherFRResponseInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `conecs_id` | `str` | Optional | Meal Voucher conecsId. |
| `siret` | `str` | Optional | Meal Voucher siret. |
| `sub_types` | `List[str]` | Optional | The list of additional payment methods. |

## Example

```python
from adyen.models.meal_voucher_fr_response_info import MealVoucherFRResponseInfo

meal_voucher_fr_response_info = MealVoucherFRResponseInfo(
    conecs_id='conecsId4',
    siret='siret0',
    sub_types=[
        'subTypes9',
        'subTypes0',
        'subTypes1'
    ]
)
```

