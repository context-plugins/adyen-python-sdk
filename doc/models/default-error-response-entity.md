
# Default Error Response Entity

Standardized error response following RFC-7807 format

Find out more here: [https://www.rfc-editor.org/rfc/rfc7807](https://www.rfc-editor.org/rfc/rfc7807)

*This model accepts additional fields of type Any.*

## Structure

`DefaultErrorResponseEntity`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `detail` | `str` | Optional | A human-readable explanation specific to this occurrence of the problem. |
| `error_code` | `str` | Optional | Unique business error code. |
| `instance` | `str` | Optional | A URI that identifies the specific occurrence of the problem if applicable. |
| `invalid_fields` | [`List[InvalidField]`](../../doc/models/invalid-field.md) | Optional | Array of fields with validation errors when applicable. |
| `request_id` | `str` | Optional | The unique reference for the request. |
| `status` | `int` | Optional | The HTTP status code. |
| `title` | `str` | Optional | A short, human-readable summary of the problem type. |
| `mtype` | `str` | Optional | A URI that identifies the validation error type. It points to human-readable documentation for the problem type. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.default_error_response_entity import DefaultErrorResponseEntity
from adyen.models.invalid_field import InvalidField

default_error_response_entity = DefaultErrorResponseEntity(
    detail='detail8',
    error_code='errorCode8',
    instance='instance8',
    invalid_fields=[
        InvalidField(
            message='message6',
            name='name6',
            value='value8',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        InvalidField(
            message='message6',
            name='name6',
            value='value8',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    request_id='requestId4',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

