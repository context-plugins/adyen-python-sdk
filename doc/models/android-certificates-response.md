
# Android Certificates Response

*This model accepts additional fields of type Any.*

## Structure

`AndroidCertificatesResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `data` | [`List[AndroidCertificate]`](../../doc/models/android-certificate.md) | Optional | Uploaded Android certificates for Android payment terminals. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from adyen.models.android_certificate import AndroidCertificate
from adyen.models.android_certificates_response import AndroidCertificatesResponse

android_certificates_response = AndroidCertificatesResponse(
    data=[
        AndroidCertificate(
            id='id0',
            description='description0',
            extension='extension6',
            name='name0',
            not_after=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
            not_before=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        AndroidCertificate(
            id='id0',
            description='description0',
            extension='extension6',
            name='name0',
            not_after=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
            not_before=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        AndroidCertificate(
            id='id0',
            description='description0',
            extension='extension6',
            name='name0',
            not_after=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
            not_before=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

