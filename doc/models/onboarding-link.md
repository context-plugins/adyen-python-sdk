
# Onboarding Link

## Structure

`OnboardingLink`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `url` | `str` | Optional | The URL of the hosted onboarding page where you need to redirect your user. This URL:<br><br>- Expires after 4 minutes.<br><br>- Can only be used once.<br><br>- Can only be clicked once by the user.<br><br>If the link expires, you need to create a new link. |

## Example

```python
from adyen.models.onboarding_link import OnboardingLink

onboarding_link = OnboardingLink(
    url='url2'
)
```

