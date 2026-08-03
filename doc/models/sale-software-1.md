
# Sale Software 1

Information related to the software of the Sale System which manages the Sale to POI protocol.

*This model accepts additional fields of type Any.*

## Structure

`SaleSoftware1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `manufacturer_id` | `str` | Required | Identification of the Manufacturer.<br><br>**Constraints**: *Pattern*: `^.+$` |
| `application_name` | `str` | Required | Name of the software product.<br><br>**Constraints**: *Pattern*: `^.+$` |
| `software_version` | `str` | Required | Version of the software product.<br><br>**Constraints**: *Pattern*: `^.+$` |
| `certification_code` | `str` | Required | Certification code of the software which manages the Sale to POI protocol.<br><br>**Constraints**: *Pattern*: `^.+$` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.sale_software_1 import SaleSoftware1

sale_software_1 = SaleSoftware1(
    manufacturer_id='ManufacturerID8',
    application_name='ApplicationName4',
    software_version='SoftwareVersion4',
    certification_code='CertificationCode8',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

