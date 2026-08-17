
# Android Certificate

## Structure

`AndroidCertificate`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `description` | `str` | Optional | The description that was provided when uploading the certificate. |
| `extension` | `str` | Optional | The file format of the certificate, as indicated by the file extension. For example, **.cert** or **.pem**. |
| `id` | `str` | Required | The unique identifier of the certificate. |
| `name` | `str` | Optional | The file name of the certificate. For example, **mycert**. |
| `not_after` | `datetime` | Optional | The date when the certificate stops to be valid. |
| `not_before` | `datetime` | Optional | The date when the certificate starts to be valid. |
| `status` | `str` | Optional | The status of the certificate. |

## Example

```python
import dateutil.parser

from adyen.models.android_certificate import AndroidCertificate

android_certificate = AndroidCertificate(
    id='id0',
    description='description0',
    extension='extension6',
    name='name0',
    not_after=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    not_before=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
)
```

