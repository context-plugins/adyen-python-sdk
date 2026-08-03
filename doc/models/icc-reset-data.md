
# Icc Reset Data

*This model accepts additional fields of type Any.*

## Structure

`IccResetData`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `atr_value` | `str` | Optional | **Constraints**: *Pattern*: `^.{1,100}$` |
| `card_status_words` | `str` | Optional | **Constraints**: *Pattern*: `^.{2,2}$` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.icc_reset_data import IccResetData

icc_reset_data = IccResetData(
    atr_value='ATRValue2',
    card_status_words='CardStatusWords2',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

