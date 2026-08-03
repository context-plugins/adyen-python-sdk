
# Meal Voucher Fr Info 1

Details to provide if `type` is **mealVoucher_FR**.

*This model accepts additional fields of type Any.*

## Structure

`MealVoucherFrInfo1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `conecs_id` | `str` | Required | Meal Voucher conecsId. Format: digits only |
| `siret` | `str` | Required | Meal Voucher siret. Format: 14 digits.<br><br>**Constraints**: *Minimum Length*: `14`, *Maximum Length*: `14` |
| `sub_types` | `List[str]` | Required | The list of additional payment methods. Allowed values: **mealVoucher_FR_endenred**, **mealVoucher_FR_groupeup**, **mealVoucher_FR_natixis**, **mealVoucher_FR_sodexo**. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.meal_voucher_fr_info_1 import MealVoucherFrInfo1

meal_voucher_fr_info_1 = MealVoucherFrInfo1(
    conecs_id='conecsId4',
    siret='siret8',
    sub_types=[
        'subTypes1'
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

