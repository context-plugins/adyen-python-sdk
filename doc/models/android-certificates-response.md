
# Android Certificates Response

## Structure

`AndroidCertificatesResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `data` | [`List[AndroidCertificate]`](../../doc/models/android-certificate.md) | Optional | Uploaded Android certificates for Android payment terminals. |

## Example

```python
import dateutil.parser

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
            not_before=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
        ),
        AndroidCertificate(
            id='id0',
            description='description0',
            extension='extension6',
            name='name0',
            not_after=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
            not_before=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
        ),
        AndroidCertificate(
            id='id0',
            description='description0',
            extension='extension6',
            name='name0',
            not_after=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
            not_before=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
        )
    ]
)
```

