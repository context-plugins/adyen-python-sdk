
# Onboarding Themes

*This model accepts additional fields of type Any.*

## Structure

`OnboardingThemes`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `next` | `str` | Optional | The next page. Only present if there is a next page. |
| `previous` | `str` | Optional | The previous page. Only present if there is a previous page. |
| `themes` | [`List[OnboardingTheme]`](../../doc/models/onboarding-theme.md) | Required | List of onboarding themes. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from adyen.models.onboarding_theme import OnboardingTheme
from adyen.models.onboarding_themes import OnboardingThemes

onboarding_themes = OnboardingThemes(
    themes=[
        OnboardingTheme(
            created_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
            id='id2',
            properties={
                'key0': 'properties0'
            },
            description='description8',
            updated_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    next='next4',
    previous='previous6',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

