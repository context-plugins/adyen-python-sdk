
# Vias Name

## Structure

`ViasName`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `first_name` | `str` | Optional | The first name.<br><br>**Constraints**: *Maximum Length*: `80` |
| `gender` | [`GenderEnum`](../../doc/models/gender-enum.md) | Optional | The gender.<br><br>> The following values are permitted: `MALE`, `FEMALE`, `UNKNOWN`.<br><br>**Constraints**: *Maximum Length*: `1` |
| `infix` | `str` | Optional | The name's infix, if applicable.<br><br>> A maximum length of twenty (20) characters is imposed.<br><br>**Constraints**: *Maximum Length*: `20` |
| `last_name` | `str` | Optional | The last name.<br><br>**Constraints**: *Maximum Length*: `80` |

## Example

```python
from adyen.models.gender_enum import GenderEnum
from adyen.models.vias_name import ViasName

vias_name = ViasName(
    first_name='firstName8',
    gender=GenderEnum.UNKNOWN,
    infix='infix6',
    last_name='lastName6'
)
```

