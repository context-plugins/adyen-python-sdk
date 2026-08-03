
# Href 5

A short-lived URL that redirects the user to the iDEAL profile registration page.

*This model accepts additional fields of type Any.*

## Structure

`Href5`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `href` | `str` | Required | The full URL for the redirection. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.href_5 import Href5

href_5 = Href5(
    href='https://someUrl',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

