
# Wifi Profiles 2

Remote Wi-Fi profiles for WPA and WPA2 PSK and EAP Wi-Fi networks.

## Structure

`WifiProfiles2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `profiles` | [`List[Profile]`](../../doc/models/profile.md) | Optional | List of remote Wi-Fi profiles. |
| `settings` | [`Settings1`](../../doc/models/settings-1.md) | Optional | General Wi-Fi settings. |

## Example

```python
from adyen.models.profile import Profile
from adyen.models.settings_1 import Settings1
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
            eap='eap0'
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
            eap='eap0'
        )
    ],
    settings=Settings1(
        band='band0',
        roaming=False,
        timeout=124
    )
)
```

