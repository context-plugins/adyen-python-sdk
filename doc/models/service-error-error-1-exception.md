
# Service Error Error 1 Exception

## Structure

`ServiceErrorError1Exception`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `error_code` | `str` | Optional | The error code mapped to the error message. |
| `error_type` | `str` | Optional | The category of the error. |
| `message` | `str` | Optional | A short explanation of the issue. |
| `psp_reference` | `str` | Optional | The PSP reference of the payment. |
| `status` | `int` | Optional | The HTTP response status. |

## Example

```python
try:
    # make the API call
except ServiceErrorError1Exception as e:
    print(e)
except APIException as e:
    print(e)
```

