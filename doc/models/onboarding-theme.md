
# Onboarding Theme

## Structure

`OnboardingTheme`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `created_at` | `datetime` | Required | The creation date of the theme. |
| `description` | `str` | Optional | The description of the theme. |
| `id` | `str` | Required | The unique identifier of the theme. |
| `properties` | `Dict[str, str]` | Required | The properties of the theme. |
| `updated_at` | `datetime` | Optional | The date when the theme was last updated. |

## Example

```python
import dateutil.parser

from adyen.models.onboarding_theme import OnboardingTheme

onboarding_theme = OnboardingTheme(
    created_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    id='id2',
    properties={
        'key0': 'properties0',
        'key1': 'properties1',
        'key2': 'properties2'
    },
    description='description2',
    updated_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
)
```

