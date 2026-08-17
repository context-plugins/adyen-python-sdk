
# Android Apps Response

## Structure

`AndroidAppsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `data` | [`List[AndroidApp]`](../../doc/models/android-app.md) | Optional | Apps uploaded for Android payment terminals. |

## Example

```python
from adyen.models.android_app import AndroidApp
from adyen.models.android_app_error import AndroidAppError
from adyen.models.android_apps_response import AndroidAppsResponse
from adyen.models.status_7_enum import Status7Enum

android_apps_response = AndroidAppsResponse(
    data=[
        AndroidApp(
            id='id0',
            status=Status7Enum.INVALID,
            description='description0',
            error_code='errorCode6',
            errors=[
                AndroidAppError(
                    error_code='errorCode6',
                    terminal_models=[
                        'terminalModels3',
                        'terminalModels4'
                    ]
                )
            ],
            label='label0',
            package_name='packageName6'
        ),
        AndroidApp(
            id='id0',
            status=Status7Enum.INVALID,
            description='description0',
            error_code='errorCode6',
            errors=[
                AndroidAppError(
                    error_code='errorCode6',
                    terminal_models=[
                        'terminalModels3',
                        'terminalModels4'
                    ]
                )
            ],
            label='label0',
            package_name='packageName6'
        )
    ]
)
```

