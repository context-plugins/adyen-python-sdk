
# Service Error 1

## Structure

`ServiceError1`

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
from adyen.models.service_error_1 import ServiceError1

service_error_1 = ServiceError1(
    error_code='errorCode6',
    error_type='errorType0',
    message='message0',
    psp_reference='pspReference8',
    status=252
)
```

