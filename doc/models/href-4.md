
# Href 4

A short-lived URL that redirects the user to the iDEAL page that is required for authentication.

*This model accepts additional fields of type Any.*

## Structure

`Href4`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `href` | `str` | Required | The full URL for the redirection. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.href_4 import Href4

href_4 = Href4(
    href='https://someUrl',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

