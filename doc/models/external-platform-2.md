
# External Platform 2

*This model accepts additional fields of type Any.*

## Structure

`ExternalPlatform2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `integrator` | `str` | Optional | External platform integrator. |
| `name` | `str` | Optional | Name of the field. For example, Name of External Platform. |
| `version` | `str` | Optional | Version of the field. For example, Version of External Platform. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.external_platform_2 import ExternalPlatform2

external_platform_2 = ExternalPlatform2(
    integrator='integrator2',
    name='name6',
    version='version2',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

