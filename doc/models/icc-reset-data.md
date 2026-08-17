
# ICC Reset Data

## Structure

`ICCResetData`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `atr_value` | `str` | Optional | **Constraints**: *Pattern*: `^.{1,100}$` |
| `card_status_words` | `str` | Optional | **Constraints**: *Pattern*: `^.{2,2}$` |

## Example

```python
from adyen.models.icc_reset_data import ICCResetData

icc_reset_data = ICCResetData(
    atr_value='ATRValue2',
    card_status_words='CardStatusWords2'
)
```

