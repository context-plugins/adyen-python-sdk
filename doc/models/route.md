
# Route

*This model accepts additional fields of type Any.*

## Structure

`Route`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `link` | `str` | Required | The redirection link. You can use this link to redirect the user to the open banking flow when the user selects it.<br><br>**Constraints**: *Minimum Length*: `1` |
| `provider` | [`Provider`](../../doc/models/provider.md) | Required | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.provider import Provider
from adyen.models.route import Route

route = Route(
    link='link2',
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
```

