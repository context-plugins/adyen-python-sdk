
# Birth Data 1

The individual's birth information.

## Structure

`BirthData1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `date_of_birth` | `str` | Optional | The individual's date of birth, in YYYY-MM-DD format. |

## Example

```python
from adyen.models.birth_data_1 import BirthData1

birth_data_1 = BirthData1(
    date_of_birth='dateOfBirth0'
)
```

