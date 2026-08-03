
# Predefined Content 2

*This model accepts additional fields of type Any.*

## Structure

`PredefinedContent2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `reference_id` | `str` | Required | Identification of a predefined message to display or print.<br><br>**Constraints**: *Pattern*: `^.+$` |
| `language` | `str` | Optional | Identification of a language.<br><br>**Constraints**: *Pattern*: `^[a-z]{2,2}$` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.predefined_content_2 import PredefinedContent2

predefined_content_2 = PredefinedContent2(
    reference_id='ReferenceID8',
    language='Language4',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

