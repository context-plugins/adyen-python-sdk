
# Profile

*This model accepts additional fields of type Any.*

## Structure

`Profile`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `auth_type` | `str` | Required | The type of Wi-Fi network. Possible values: **wpa-psk**, **wpa2-psk**, **wpa-eap**, **wpa2-eap**. |
| `auto_wifi` | `bool` | Optional | Indicates whether to automatically select the best authentication method available. Does not work on older terminal models. |
| `bss_type` | `str` | Required | Use **infra** for infrastructure-based networks. This applies to most networks. Use **adhoc** only if the communication is p2p-based between base stations. |
| `channel` | `int` | Optional | The channel number of the Wi-Fi network. The recommended setting is **0** for automatic channel selection. |
| `default_profile` | `bool` | Optional | Indicates whether this is your preferred wireless network. If **true**, the terminal will try connecting to this network first. |
| `domain_suffix` | `str` | Optional | Specifies the server domain name for EAP-TLS and EAP-PEAP WiFi profiles on Android 11 and above. |
| `eap` | `str` | Optional | For `authType` **wpa-eap** or **wpa2-eap**. Possible values: **tls**, **peap**, **leap**, **fast** |
| `eap_ca_cert` | [`File`](../../doc/models/file.md) | Optional | - |
| `eap_client_cert` | [`File`](../../doc/models/file.md) | Optional | - |
| `eap_client_key` | [`File`](../../doc/models/file.md) | Optional | - |
| `eap_client_pwd` | `str` | Optional | For `eap` **tls**. The password of the RSA key file, if that file is password-protected. |
| `eap_identity` | `str` | Optional | For `authType` **wpa-eap** or **wpa2-eap**. The EAP-PEAP username from your MS-CHAP account. Must match the configuration of your RADIUS server. |
| `eap_intermediate_cert` | [`File`](../../doc/models/file.md) | Optional | - |
| `eap_pwd` | `str` | Optional | For `eap` **peap**. The EAP-PEAP password from your MS-CHAP account. Must match the configuration of your RADIUS server. |
| `hidden_ssid` | `bool` | Optional | Indicates if the network doesn't broadcast its SSID. Mandatory for Android terminals, because these terminals rely on this setting to be able to connect to any network. |
| `name` | `str` | Optional | Your name for the Wi-Fi profile. |
| `psk` | `str` | Optional | For `authType` **wpa-psk or **wpa2-psk**. The password to the wireless network. |
| `ssid` | `str` | Required | The name of the wireless network. |
| `wsec` | `str` | Required | The type of encryption. Possible values: **auto**, **ccmp** (recommended), **tkip** |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.profile import Profile

profile = Profile(
    auth_type='authType0',
    bss_type='bssType6',
    ssid='ssid8',
    wsec='wsec4',
    auto_wifi=False,
    channel=114,
    default_profile=False,
    domain_suffix='domainSuffix4',
    eap='eap2',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

