
# Create Allowed Origin Request

*This model accepts additional fields of type Any.*

## Structure

`CreateAllowedOriginRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `links` | [`Links2`](../../doc/models/links-2.md) | Optional | - |
| `domain` | `str` | Required | Domain of the allowed origin. |
| `id` | `str` | Optional | Unique identifier of the allowed origin. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.create_allowed_origin_request import CreateAllowedOriginRequest
from adyen.models.links_2 import Links2
from adyen.models.mself import Self

create_allowed_origin_request = CreateAllowedOriginRequest(
    domain='https://adyen.com',
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
    id='id8',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

