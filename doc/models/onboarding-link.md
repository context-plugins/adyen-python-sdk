
# Onboarding Link

*This model accepts additional fields of type Any.*

## Structure

`OnboardingLink`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `url` | `str` | Optional | The URL of the hosted onboarding page where you need to redirect your user. This URL:<br><br>- Expires after 4 minutes.<br><br>- Can only be used once.<br><br>- Can only be clicked once by the user.<br><br>If the link expires, you need to create a new link. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.onboarding_link import OnboardingLink

onboarding_link = OnboardingLink(
    url='url2',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

