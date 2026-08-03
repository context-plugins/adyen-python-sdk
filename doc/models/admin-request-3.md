
# Admin Request 3

*This model accepts additional fields of type Any.*

## Structure

`AdminRequest3`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `service_identification` | `str` | Optional | Identification of the administrative service to process.<br><br>**Constraints**: *Pattern*: `^.+$` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.admin_request_3 import AdminRequest3

admin_request_3 = AdminRequest3(
    service_identification='ServiceIdentification2',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

