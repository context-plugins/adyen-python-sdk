
# Admin Request

Empty.
Content of the Custom Admin Request message.

*This model accepts additional fields of type Any.*

## Structure

`AdminRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `service_identification` | `str` | Optional | Identification of the administrative service to process.<br><br>**Constraints**: *Pattern*: `^.+$` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.admin_request import AdminRequest

admin_request = AdminRequest(
    service_identification='ServiceIdentification4',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

