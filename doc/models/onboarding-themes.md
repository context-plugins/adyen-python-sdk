
# Onboarding Themes

## Structure

`OnboardingThemes`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `next` | `str` | Optional | The next page. Only present if there is a next page. |
| `previous` | `str` | Optional | The previous page. Only present if there is a previous page. |
| `themes` | [`List[OnboardingTheme]`](../../doc/models/onboarding-theme.md) | Required | List of onboarding themes. |

## Example

```python
import dateutil.parser

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
            updated_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
        )
    ],
    next='next4',
    previous='previous6'
)
```

