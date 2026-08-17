
# App Identifier Info 1

The app identifier information containing iOS scheme and Android package ID.

## Structure

`AppIdentifierInfo1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `android_package_id` | `str` | Optional | The Android package identifier for this app. |
| `ios_scheme` | `str` | Optional | The iOS URL scheme for this app. |

## Example

```python
from adyen.models.app_identifier_info_1 import AppIdentifierInfo1

app_identifier_info_1 = AppIdentifierInfo1(
    android_package_id='androidPackageId4',
    ios_scheme='iosScheme4'
)
```

