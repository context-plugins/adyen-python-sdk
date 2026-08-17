
# Account Verification Routes Response

## Structure

`AccountVerificationRoutesResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `routes` | [`List[Route]`](../../doc/models/route.md) | Required | This array lists available open banking redirection links, each with its associated provider metadata. |

## Example

```python
from adyen.models.account_verification_routes_response import AccountVerificationRoutesResponse
from adyen.models.provider_2 import Provider2
from adyen.models.route import Route

account_verification_routes_response = AccountVerificationRoutesResponse(
    routes=[
        Route(
            link='link6',
            provider=Provider2(
                logo_url='logoURL6',
                name='name8'
            )
        )
    ]
)
```

