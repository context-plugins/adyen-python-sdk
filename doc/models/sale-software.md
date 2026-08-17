
# Sale Software

Information related to the software of the Sale System which manages the NEXO Sale to POI protocol.

## Structure

`SaleSoftware`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `manufacturer_id` | `str` | Required | Identification of the Manufacturer.<br><br>**Constraints**: *Pattern*: `^.+$` |
| `application_name` | `str` | Required | Name of the software product.<br><br>**Constraints**: *Pattern*: `^.+$` |
| `software_version` | `str` | Required | Version of the software product.<br><br>**Constraints**: *Pattern*: `^.+$` |
| `certification_code` | `str` | Required | Certification code of the software which manages the Sale to POI protocol.<br><br>**Constraints**: *Pattern*: `^.+$` |

## Example

```python
from adyen.models.sale_software import SaleSoftware

sale_software = SaleSoftware(
    manufacturer_id='ManufacturerID4',
    application_name='ApplicationName2',
    software_version='SoftwareVersion0',
    certification_code='CertificationCode4'
)
```

