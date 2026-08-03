
# Uninstall Android Certificate Details

*This model accepts additional fields of type Any.*

## Structure

`UninstallAndroidCertificateDetails`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `certificate_id` | `str` | Optional | The unique identifier of the certificate to be uninstalled. |
| `mtype` | [`Type82`](../../doc/models/type-82.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.type_82 import Type82
from adyen.models.uninstall_android_certificate_details import UninstallAndroidCertificateDetails

uninstall_android_certificate_details = UninstallAndroidCertificateDetails(
    certificate_id='certificateId8',
    mtype=Type82.UNINSTALLANDROIDCERTIFICATE,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

