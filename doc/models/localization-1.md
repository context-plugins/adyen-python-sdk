
# Localization 1

Settings for localization.

*This model accepts additional fields of type Any.*

## Structure

`Localization1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `language` | `str` | Optional | Language of the terminal. |
| `secondary_language` | `str` | Optional | Secondary language of the terminal. |
| `timezone` | `str` | Optional | The time zone of the terminal. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.localization_1 import Localization1

localization_1 = Localization1(
    language='language0',
    secondary_language='secondaryLanguage6',
    timezone='timezone8',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

