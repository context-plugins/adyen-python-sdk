
# Ideal Auth Link Response

## Structure

`IdealAuthLinkResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `redirect_url` | [`Href3`](../../doc/models/href-3.md) | Optional | A short-lived URL that redirects the user to the iDEAL profile management page. |

## Example

```python
from adyen.models.href_3 import Href3
from adyen.models.ideal_auth_link_response import IdealAuthLinkResponse

ideal_auth_link_response = IdealAuthLinkResponse(
    redirect_url=Href3(
        href='href8'
    )
)
```

