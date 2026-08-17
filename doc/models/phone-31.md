
# Phone 31

The phone number of the account holder.

## Structure

`Phone31`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `number` | `str` | Required | The full phone number provided as a single string.<br>For example, **"0031 6 11 22 33 44"**, **"+316/1122-3344"**,<br><br>or **"(0031) 611223344"**. |
| `mtype` | [`Type410Enum`](../../doc/models/type-410-enum.md) | Required | Type of phone number.<br>Possible values:<br>**Landline**, **Mobile**. |

## Example

```python
from adyen.models.phone_31 import Phone31
from adyen.models.type_410_enum import Type410Enum

phone_31 = Phone31(
    number='number6',
    mtype=Type410Enum.LANDLINE
)
```

