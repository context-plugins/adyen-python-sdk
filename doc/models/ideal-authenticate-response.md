
# Ideal Authenticate Response

*This model accepts additional fields of type Any.*

## Structure

`IdealAuthenticateResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `redirect_url` | [`Href`](../../doc/models/href.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.href import Href
from adyen.models.ideal_authenticate_response import IdealAuthenticateResponse

ideal_authenticate_response = IdealAuthenticateResponse(
    redirect_url=Href(
        href='href8',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

