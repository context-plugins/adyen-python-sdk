
# Meal Voucher FR Info 1

Details to provide if `type` is **mealVoucher_FR**.

## Structure

`MealVoucherFRInfo1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `conecs_id` | `str` | Required | Meal Voucher conecsId. Format: digits only |
| `siret` | `str` | Required | Meal Voucher siret. Format: 14 digits.<br><br>**Constraints**: *Minimum Length*: `14`, *Maximum Length*: `14` |
| `sub_types` | `List[str]` | Required | The list of additional payment methods. Allowed values: **mealVoucher_FR_endenred**, **mealVoucher_FR_groupeup**, **mealVoucher_FR_natixis**, **mealVoucher_FR_sodexo**. |

## Example

```python
from adyen.models.meal_voucher_fr_info_1 import MealVoucherFRInfo1

meal_voucher_fr_info_1 = MealVoucherFRInfo1(
    conecs_id='conecsId4',
    siret='siret8',
    sub_types=[
        'subTypes1'
    ]
)
```

