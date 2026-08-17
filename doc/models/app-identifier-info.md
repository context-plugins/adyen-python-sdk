
# App Identifier Info

## Structure

`AppIdentifierInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `android_package_id` | `str` | Optional | The Android package identifier for this app. |
| `ios_scheme` | `str` | Optional | The iOS URL scheme for this app. |

## Example

```python
from adyen.models.app_identifier_info import AppIdentifierInfo

app_identifier_info = AppIdentifierInfo(
    android_package_id='androidPackageId2',
    ios_scheme='iosScheme2'
)
```

