
# Android App

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
| `status` | [`Status7Enum`](../../doc/models/status-7-enum.md) | Required | The status of the app. Possible values:<br><br>* `processing`: the app is being signed and converted to a format that the terminal can handle.<br>* `error`: something went wrong. Check that the app matches the [requirements](https://docs.adyen.com/point-of-sale/android-terminals/app-requirements).<br>* `invalid`: there is something wrong with the APK file of the app.<br>* `ready`: the app has been signed and converted.<br>* `archived`: the app is no longer available. |
| `version_code` | `int` | Optional | The version number of the app. |
| `version_name` | `str` | Optional | The app version number that is shown on the terminal. |

## Example

```python
from adyen.models.android_app import AndroidApp
from adyen.models.android_app_error import AndroidAppError
from adyen.models.status_7_enum import Status7Enum

android_app = AndroidApp(
    id='id4',
    status=Status7Enum.READY,
    description='description4',
    error_code='errorCode0',
    errors=[
        AndroidAppError(
            error_code='errorCode6',
            terminal_models=[
                'terminalModels3',
                'terminalModels4'
            ]
        )
    ],
    label='label4',
    package_name='packageName0'
)
```

