
# Allowed Origins Response

*This model accepts additional fields of type Any.*

## Structure

`AllowedOriginsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `data` | [`List[AllowedOrigin]`](../../doc/models/allowed-origin.md) | Optional | List of allowed origins. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.allowed_origin import AllowedOrigin
from adyen.models.allowed_origins_response import AllowedOriginsResponse
from adyen.models.links_2 import Links2
from adyen.models.mself import Self

allowed_origins_response = AllowedOriginsResponse(
    data=[
        AllowedOrigin(
            domain='domain6',
            links=Links2(
                mself=Self(
                    href='href0',
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                ),
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            id='id0',
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

