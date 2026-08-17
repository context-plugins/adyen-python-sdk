
# Profile Registration Response

## Structure

`ProfileRegistrationResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `redirect_url` | [`Href5`](../../doc/models/href-5.md) | Optional | A short-lived URL that redirects the user to the iDEAL profile registration page. |

## Example

```python
from adyen.models.href_5 import Href5
from adyen.models.profile_registration_response import ProfileRegistrationResponse

profile_registration_response = ProfileRegistrationResponse(
    redirect_url=Href5(
        href='href8'
    )
)
```

