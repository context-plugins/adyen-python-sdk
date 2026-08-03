
# Predefined Content 1

Reference of a predefined message to display or print.
Mandatory, if `OutputFormat` is MessageRef, not allowed otherwise.

*This model accepts additional fields of type Any.*

## Structure

`PredefinedContent1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `reference_id` | `str` | Required | Identification of a predefined message to display or print.<br><br>**Constraints**: *Pattern*: `^.+$` |
| `language` | `str` | Optional | Identification of a language.<br><br>**Constraints**: *Pattern*: `^[a-z]{2,2}$` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.predefined_content_1 import PredefinedContent1

predefined_content_1 = PredefinedContent1(
    reference_id='ReferenceID8',
    language='Language4',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

