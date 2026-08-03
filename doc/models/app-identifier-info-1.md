
# App Identifier Info 1

The app identifier information containing iOS scheme and Android package ID.

*This model accepts additional fields of type Any.*

## Structure

`AppIdentifierInfo1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `android_package_id` | `str` | Optional | The Android package identifier for this app. |
| `ios_scheme` | `str` | Optional | The iOS URL scheme for this app. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.app_identifier_info_1 import AppIdentifierInfo1

app_identifier_info_1 = AppIdentifierInfo1(
    android_package_id='androidPackageId4',
    ios_scheme='iosScheme4',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

