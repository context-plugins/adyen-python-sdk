
# Installed Ap Ks

*This model accepts additional fields of type Any.*

## Structure

`InstalledApKs`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `confirmation_date` | `datetime` | Optional | The date and time when the app was installed. |
| `package_name` | `str` | Optional | The package name of the app. |
| `version_name` | `str` | Optional | The version name of the app. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from adyen.models.installed_ap_ks import InstalledApKs

installed_ap_ks = InstalledApKs(
    confirmation_date=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    package_name='packageName2',
    version_name='versionName2',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

