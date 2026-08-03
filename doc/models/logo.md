
# Logo

*This model accepts additional fields of type Any.*

## Structure

`Logo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `data` | `str` | Optional | The image file, converted to a Base64-encoded string, of the logo to be shown on the terminal.<br><br>**Constraints**: *Maximum Length*: `350000` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.logo import Logo

logo = Logo(
    data='data4',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

