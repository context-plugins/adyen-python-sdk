
# Wifi Profiles 2

Remote Wi-Fi profiles for WPA and WPA2 PSK and EAP Wi-Fi networks.

*This model accepts additional fields of type Any.*

## Structure

`WifiProfiles2`

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
from adyen.models.wifi_profiles_2 import WifiProfiles2

wifi_profiles_2 = WifiProfiles2(
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
        ),
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

