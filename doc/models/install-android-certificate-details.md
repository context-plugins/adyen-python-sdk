
# Install Android Certificate Details

*This model accepts additional fields of type Any.*

## Structure

`InstallAndroidCertificateDetails`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `certificate_id` | `str` | Optional | The unique identifier of the certificate to be installed. |
| `mtype` | [`Type42`](../../doc/models/type-42.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.install_android_certificate_details import InstallAndroidCertificateDetails
from adyen.models.type_42 import Type42

install_android_certificate_details = InstallAndroidCertificateDetails(
    certificate_id='certificateId2',
    mtype=Type42.INSTALLANDROIDCERTIFICATE,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

