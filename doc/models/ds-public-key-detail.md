
# DS Public Key Detail

## Structure

`DSPublicKeyDetail`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `brand` | `str` | Optional | Card brand. |
| `directory_server_id` | `str` | Optional | Directory Server (DS) identifier. |
| `from_sdk_version` | `str` | Optional | The version of the mobile 3D Secure 2 SDK. For the possible values, refer to the versions in [Adyen 3DS2 Android](https://github.com/Adyen/adyen-3ds2-android/releases) and [Adyen 3DS2 iOS](https://github.com/Adyen/adyen-3ds2-ios/releases). |
| `public_key` | `str` | Optional | Public key. The 3D Secure 2 SDK encrypts the device information by using the DS public key. |
| `root_certificates` | `str` | Optional | Directory Server root certificates. The 3D Secure 2 SDK verifies the ACS signed content using the rootCertificates. |

## Example

```python
from adyen.models.ds_public_key_detail import DSPublicKeyDetail

ds_public_key_detail = DSPublicKeyDetail(
    brand='brand8',
    directory_server_id='directoryServerId2',
    from_sdk_version='fromSDKVersion0',
    public_key='publicKey2',
    root_certificates='rootCertificates6'
)
```

