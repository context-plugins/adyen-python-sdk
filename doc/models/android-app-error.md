
# Android App Error

## Structure

`AndroidAppError`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `error_code` | `str` | Optional | The error code of the Android app with the `status` of either **error** or **invalid**. |
| `terminal_models` | `List[str]` | Optional | The list of payment terminal models to which the returned `errorCode` applies. |

## Example

```python
from adyen.models.android_app_error import AndroidAppError

android_app_error = AndroidAppError(
    error_code='errorCode8',
    terminal_models=[
        'terminalModels5',
        'terminalModels6'
    ]
)
```

