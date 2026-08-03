
# App Identifier Info

*This model accepts additional fields of type Any.*

## Structure

`AppIdentifierInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `android_package_id` | `str` | Optional | The Android package identifier for this app. |
| `ios_scheme` | `str` | Optional | The iOS URL scheme for this app. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.app_identifier_info import AppIdentifierInfo

app_identifier_info = AppIdentifierInfo(
    android_package_id='androidPackageId2',
    ios_scheme='iosScheme2',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

