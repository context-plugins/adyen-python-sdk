
# Android Apps Response

*This model accepts additional fields of type Any.*

## Structure

`AndroidAppsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `data` | [`List[AndroidApp]`](../../doc/models/android-app.md) | Optional | Apps uploaded for Android payment terminals. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.android_app import AndroidApp
from adyen.models.android_app_error import AndroidAppError
from adyen.models.android_apps_response import AndroidAppsResponse
from adyen.models.status_15 import Status15

android_apps_response = AndroidAppsResponse(
    data=[
        AndroidApp(
            id='id0',
            status=Status15.INVALID,
            description='description0',
            error_code='errorCode6',
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
            label='label0',
            package_name='packageName6',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        AndroidApp(
            id='id0',
            status=Status15.INVALID,
            description='description0',
            error_code='errorCode6',
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
            label='label0',
            package_name='packageName6',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

