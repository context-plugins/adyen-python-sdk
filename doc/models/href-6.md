
# Href 6

The URL to where the user must be redirected after a payment has been canceled.

*This model accepts additional fields of type Any.*

## Structure

`Href6`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `href` | `str` | Required | The full URL for the redirection. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.href_6 import Href6

href_6 = Href6(
    href='https://someUrl',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

