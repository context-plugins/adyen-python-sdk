
# Localization

*This model accepts additional fields of type Any.*

## Structure

`Localization`

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

from adyen.models.localization import Localization

localization = Localization(
    language='language0',
    secondary_language='secondaryLanguage6',
    timezone='timezone8',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

