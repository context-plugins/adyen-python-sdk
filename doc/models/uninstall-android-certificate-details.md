
# Uninstall Android Certificate Details

## Structure

`UninstallAndroidCertificateDetails`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `certificate_id` | `str` | Optional | The unique identifier of the certificate to be uninstalled. |
| `mtype` | [`Type81Enum`](../../doc/models/type-81-enum.md) | Optional | Type of terminal action: Uninstall an Android certificate.<br><br>**Default**: `"UninstallAndroidCertificate"` |

## Example

```python
from adyen.models.type_81_enum import Type81Enum
from adyen.models.uninstall_android_certificate_details import UninstallAndroidCertificateDetails

uninstall_android_certificate_details = UninstallAndroidCertificateDetails(
    certificate_id='certificateId8',
    mtype=Type81Enum.UNINSTALLANDROIDCERTIFICATE
)
```

