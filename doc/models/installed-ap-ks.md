
# Installed AP Ks

## Structure

`InstalledAPKs`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `confirmation_date` | `datetime` | Optional | The date and time when the app was installed. |
| `package_name` | `str` | Optional | The package name of the app. |
| `version_name` | `str` | Optional | The version name of the app. |

## Example

```python
import dateutil.parser

from adyen.models.installed_ap_ks import InstalledAPKs

installed_ap_ks = InstalledAPKs(
    confirmation_date=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    package_name='packageName2',
    version_name='versionName2'
)
```

