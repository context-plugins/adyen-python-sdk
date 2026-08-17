
# Service Error Exception

## Structure

`ServiceErrorException`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `additional_data` | `Dict[str, str]` | Optional | Contains additional information about the payment. Some data fields are included only if you select them first. Go to **Customer Area** > **Developers** > **Additional data**. |
| `error_code` | `str` | Optional | The error code mapped to the error message. |
| `error_type` | `str` | Optional | The category of the error. |
| `message` | `str` | Optional | A short explanation of the issue. |
| `psp_reference` | `str` | Optional | The PSP reference of the payment. |
| `status` | `int` | Optional | The HTTP response status. |

## Example

```python
try:
    # make the API call
except ServiceErrorException as e:
    print(e)
except APIException as e:
    print(e)
```

