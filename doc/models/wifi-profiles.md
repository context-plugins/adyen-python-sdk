
# Wifi Profiles

*This model accepts additional fields of type Any.*

## Structure

`WifiProfiles`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `profiles` | [`List[Profile]`](../../doc/models/profile.md) | Optional | List of remote Wi-Fi profiles. |
| `settings` | [`Settings`](../../doc/models/settings.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.profile import Profile
from adyen.models.settings import Settings
from adyen.models.wifi_profiles import WifiProfiles

wifi_profiles = WifiProfiles(
    profiles=[
        Profile(
            auth_type='authType8',
            bss_type='bssType4',
            ssid='ssid6',
            wsec='wsec4',
            auto_wifi=False,
            channel=198,
            default_profile=False,
            domain_suffix='domainSuffix2',
            eap='eap0',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    settings=Settings(
        band='band0',
        roaming=False,
        timeout=124,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

