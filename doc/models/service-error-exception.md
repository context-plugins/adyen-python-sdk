
# Service Error Exception

*This model accepts additional fields of type Any.*

## Structure

`ServiceErrorException`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `error_code` | `str` | Optional | The error code mapped to the error message. |
| `error_type` | `str` | Optional | The category of the error. |
| `message` | `str` | Optional | A short explanation of the issue. |
| `psp_reference` | `str` | Optional | The PSP reference of the payment. |
| `status` | `int` | Optional | The HTTP response status. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
try:
    # make the API call
except ServiceErrorException as e:
    print(e)
except ApiException as e:
    print(e)
```

