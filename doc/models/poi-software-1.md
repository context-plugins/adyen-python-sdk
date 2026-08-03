
# Poi Software 1

*This model accepts additional fields of type Any.*

## Structure

`PoiSoftware1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `manufacturer_id` | `str` | Required | Identification of the Manufacturer. Sent in the Login Request (Response) to identify the Sale System (POI System) manufacturer during the session.<br><br>**Constraints**: *Pattern*: `^.+$` |
| `application_name` | `str` | Required | Name of the software product. Sent in the Login Request (Response) to identify the Sale System (POI System) product name during the session.<br><br>**Constraints**: *Pattern*: `^.+$` |
| `software_version` | `str` | Required | Version of the software product. Sent in the Login Request (Response) to identify the version of the Sale System (POI System) product software during the session.<br><br>**Constraints**: *Pattern*: `^.+$` |
| `certification_code` | `str` | Required | Certification code of the software which manages the Sale to POI protocol. Sent in the Login Request (Response) to get the certification code of the Sale System (POI System) product software. This code can be a software checksum or any number associated with the software.<br><br>**Constraints**: *Pattern*: `^.+$` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.poi_software_1 import PoiSoftware1

poi_software_1 = PoiSoftware1(
    manufacturer_id='ManufacturerID2',
    application_name='ApplicationName0',
    software_version='SoftwareVersion8',
    certification_code='CertificationCode2',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

