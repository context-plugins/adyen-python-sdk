
# Rest Service Error Exception

## Structure

`RestServiceErrorException`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `detail` | `str` | Required | A human-readable explanation specific to this occurrence of the problem. |
| `error_code` | `str` | Required | A code that identifies the problem type. |
| `instance` | `str` | Optional | A unique URI that identifies the specific occurrence of the problem. |
| `invalid_fields` | [`List[InvalidField]`](../../doc/models/invalid-field.md) | Optional | Detailed explanation of each validation error, when applicable. |
| `request_id` | `str` | Optional | A unique reference for the request, essentially the same as `pspReference`. |
| `response` | `Any` | Optional | JSON response payload. |
| `status` | `int` | Required | The HTTP status code. |
| `title` | `str` | Required | A short, human-readable summary of the problem type. |
| `mtype` | `str` | Required | A URI that identifies the problem type, pointing to human-readable documentation on this problem type. |

## Example

```python
try:
    # make the API call
except RestServiceErrorException as e:
    print(e)
except APIException as e:
    print(e)
```

