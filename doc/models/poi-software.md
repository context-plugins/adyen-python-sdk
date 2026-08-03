
# Poi Software

Information related to the software of the POI System which manages the Sale to POI protocol. In a session allows identifying the product features of a POI System.

*This model accepts additional fields of type Any.*

## Structure

`PoiSoftware`

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

from adyen.models.poi_software import PoiSoftware

poi_software = PoiSoftware(
    manufacturer_id='ManufacturerID6',
    application_name='ApplicationName6',
    software_version='SoftwareVersion2',
    certification_code='CertificationCode6',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

