
# Predefined Content

Reference of a predefined message to display or print.
It conveys information related to the predefined message.

*This model accepts additional fields of type Any.*

## Structure

`PredefinedContent`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `reference_id` | `str` | Required | Identification of a predefined message to display or print.<br><br>**Constraints**: *Pattern*: `^.+$` |
| `language` | `str` | Optional | Identification of a language.<br><br>**Constraints**: *Pattern*: `^[a-z]{2,2}$` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.predefined_content import PredefinedContent

predefined_content = PredefinedContent(
    reference_id='ReferenceID2',
    language='Language0',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

