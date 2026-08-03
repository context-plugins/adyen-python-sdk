
# Account Verification Routes Response

*This model accepts additional fields of type Any.*

## Structure

`AccountVerificationRoutesResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `routes` | [`List[Route]`](../../doc/models/route.md) | Required | This array lists available open banking redirection links, each with its associated provider metadata. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.account_verification_routes_response import AccountVerificationRoutesResponse
from adyen.models.provider import Provider
from adyen.models.route import Route

account_verification_routes_response = AccountVerificationRoutesResponse(
    routes=[
        Route(
            link='link6',
            provider=Provider(
                logo_url='logoURL6',
                name='name8',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

