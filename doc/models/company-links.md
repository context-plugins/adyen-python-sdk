
# Company Links

*This model accepts additional fields of type Any.*

## Structure

`CompanyLinks`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `api_credentials` | [`Href2`](../../doc/models/href-2.md) | Optional | List of allowed origins. |
| `mself` | [`Self`](../../doc/models/self.md) | Required | - |
| `users` | [`Href2`](../../doc/models/href-2.md) | Optional | List of allowed origins. |
| `webhooks` | [`Href2`](../../doc/models/href-2.md) | Optional | List of allowed origins. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.company_links import CompanyLinks
from adyen.models.href_2 import Href2
from adyen.models.mself import Self

company_links = CompanyLinks(
    mself=Self(
        href='href0',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    api_credentials=Href2(
        href='href8',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    users=Href2(
        href='href8',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    webhooks=Href2(
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

