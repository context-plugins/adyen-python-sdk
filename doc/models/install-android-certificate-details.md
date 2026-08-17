
# Install Android Certificate Details

## Structure

`InstallAndroidCertificateDetails`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `certificate_id` | `str` | Optional | The unique identifier of the certificate to be installed. |
| `mtype` | [`Type42Enum`](../../doc/models/type-42-enum.md) | Optional | Type of terminal action: Install an Android certificate.<br><br>**Default**: `"InstallAndroidCertificate"` |

## Example

```python
from adyen.models.install_android_certificate_details import InstallAndroidCertificateDetails
from adyen.models.type_42_enum import Type42Enum

install_android_certificate_details = InstallAndroidCertificateDetails(
    certificate_id='certificateId2',
    mtype=Type42Enum.INSTALLANDROIDCERTIFICATE
)
```

