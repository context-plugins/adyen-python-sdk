
# Sca Devices Sca Associations 400 Error Exception

*This model accepts additional fields of type Any.*

## Structure

`ScaDevicesScaAssociations400ErrorException`

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
try:
    # make the API call
except ScaDevicesScaAssociations400ErrorException as e:
    print(e)
except ApiException as e:
    print(e)
```

