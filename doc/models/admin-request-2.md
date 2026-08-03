
# Admin Request 2

Content of the Admin Request message.

*This model accepts additional fields of type Any.*

## Structure

`AdminRequest2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `service_identification` | `str` | Optional | Identification of the administrative service to process.<br><br>**Constraints**: *Pattern*: `^.+$` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.admin_request_2 import AdminRequest2

admin_request_2 = AdminRequest2(
    service_identification='ServiceIdentification0',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

