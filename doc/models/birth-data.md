
# Birth Data

## Structure

`BirthData`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `date_of_birth` | `str` | Optional | The individual's date of birth, in YYYY-MM-DD format. |

## Example

```python
from adyen.models.birth_data import BirthData

birth_data = BirthData(
    date_of_birth='dateOfBirth6'
)
```

