
# Default Error Response Entity Exception

Standardized error response following RFC-7807 format

Find out more here: [https://www.rfc-editor.org/rfc/rfc7807](https://www.rfc-editor.org/rfc/rfc7807)

## Structure

`DefaultErrorResponseEntityException`

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

## Example

```python
try:
    # make the API call
except DefaultErrorResponseEntityException as e:
    print(e)
except APIException as e:
    print(e)
```

