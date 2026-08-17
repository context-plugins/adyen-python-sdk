
# Ideal Authenticate Response

## Structure

`IdealAuthenticateResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `redirect_url` | [`Href4`](../../doc/models/href-4.md) | Optional | A short-lived URL that redirects the user to the iDEAL page that is required for authentication. |

## Example

```python
from adyen.models.href_4 import Href4
from adyen.models.ideal_authenticate_response import IdealAuthenticateResponse

ideal_authenticate_response = IdealAuthenticateResponse(
    redirect_url=Href4(
        href='href8'
    )
)
```

