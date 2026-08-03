
# Onboarding Link Info

*This model accepts additional fields of type Any.*

## Structure

`OnboardingLinkInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `locale` | `str` | Optional | The language that will be used for the page, specified by a combination of two letter [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) language and [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. See possible valuesfor [marketplaces](https://docs.adyen.com/marketplaces/onboard-users/hosted#supported-languages) or [platforms](https://docs.adyen.com/platforms/onboard-users/hosted#supported-languages).<br><br>If not specified in the request or if the language is not supported, the page uses the browser language. If the browser language is not supported, the page uses **en-US** by default. |
| `redirect_url` | `str` | Optional | The URL where the user is redirected after they complete hosted onboarding. |
| `settings` | [`OnboardingLinkSettings`](../../doc/models/onboarding-link-settings.md) | Optional | - |
| `theme_id` | `str` | Optional | The unique identifier of the hosted onboarding theme. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.onboarding_link_info import OnboardingLinkInfo
from adyen.models.onboarding_link_settings import OnboardingLinkSettings

onboarding_link_info = OnboardingLinkInfo(
    locale='locale4',
    redirect_url='redirectUrl0',
    settings=OnboardingLinkSettings(
        accepted_countries=[
            'acceptedCountries9',
            'acceptedCountries0'
        ],
        allow_bank_account_format_selection=False,
        allow_debug_ui=False,
        allow_intra_region_cross_border_payout=False,
        change_legal_entity_type=False,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    theme_id='themeId0',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

