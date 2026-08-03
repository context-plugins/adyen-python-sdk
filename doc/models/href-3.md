
# Href 3

A short-lived URL that redirects the user to the iDEAL profile management page.

*This model accepts additional fields of type Any.*

## Structure

`Href3`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `href` | `str` | Required | The full URL for the redirection. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.href_3 import Href3

href_3 = Href3(
    href='https://someUrl',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

