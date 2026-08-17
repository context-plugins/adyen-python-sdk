
# Localization

## Structure

`Localization`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `language` | `str` | Optional | Language of the terminal. |
| `secondary_language` | `str` | Optional | Secondary language of the terminal. |
| `timezone` | `str` | Optional | The time zone of the terminal. |

## Example

```python
from adyen.models.localization import Localization

localization = Localization(
    language='language0',
    secondary_language='secondaryLanguage6',
    timezone='timezone8'
)
```

