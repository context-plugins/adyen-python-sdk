
# Authentication Session Request

*This model accepts additional fields of type Any.*

## Structure

`AuthenticationSessionRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `allow_origin` | `str` | Required | The URL where the component will appear. In your live environment, you must protect the URL with an SSL certificate and ensure that it starts with `https://`. |
| `policy` | [`Policy`](../../doc/models/policy.md) | Required | - |
| `product` | [`ProductType21`](../../doc/models/product-type-21.md) | Required | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.authentication_session_request import AuthenticationSessionRequest
from adyen.models.policy import Policy
from adyen.models.product_type_21 import ProductType21
from adyen.models.resource import Resource

authentication_session_request = AuthenticationSessionRequest(
    allow_origin='allowOrigin8',
    policy=Policy(
        resources=[
            Resource(
                mtype='Resource',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            )
        ],
        roles=[
            'roles8'
        ],
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    product=ProductType21.ONBOARDING,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

