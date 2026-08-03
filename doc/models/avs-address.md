
# Avs Address

*This model accepts additional fields of type Any.*

## Structure

`AvsAddress`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `street_address` | `str` | Required | The street and house number of the address.<br><br>Example: 1 Infinite Loop, Cupertino. |
| `zip` | `str` | Optional | The zip or post code of the address.<br><br>Example: CA 95014 |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.avs_address import AvsAddress

avs_address = AvsAddress(
    street_address='streetAddress0',
    zip='zip6',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

