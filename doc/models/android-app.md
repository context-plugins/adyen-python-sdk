
# Android App

*This model accepts additional fields of type Any.*

## Structure

`AndroidApp`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `description` | `str` | Optional | The description that was provided when uploading the app. The description is not shown on the terminal. |
| `error_code` | `str` | Optional | The error code of the Android app with the `status` of either **error** or **invalid**. |
| `errors` | [`List[AndroidAppError]`](../../doc/models/android-app-error.md) | Optional | The list of errors of the Android app. |
| `id` | `str` | Required | The unique identifier of the app. |
| `label` | `str` | Optional | The app name that is shown on the terminal. |
| `package_name` | `str` | Optional | The package name that uniquely identifies the Android app. |
| `status` | [`Status15`](../../doc/models/status-15.md) | Required | - |
| `version_code` | `int` | Optional | The version number of the app. |
| `version_name` | `str` | Optional | The app version number that is shown on the terminal. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.android_app import AndroidApp
from adyen.models.android_app_error import AndroidAppError
from adyen.models.status_15 import Status15

android_app = AndroidApp(
    id='id4',
    status=Status15.READY,
    description='description4',
    error_code='errorCode0',
    errors=[
        AndroidAppError(
            error_code='errorCode6',
            terminal_models=[
                'terminalModels3',
                'terminalModels4'
            ],
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    label='label4',
    package_name='packageName0',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

