
# POI System Data 1

Information related to the POI System.
Returned if the response result is Success.

## Structure

`POISystemData1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `date_time` | `datetime` | Required | Date and Time. In the response, the POI System gives its date and time to the Sale System. |
| `poi_software` | [`POISoftware`](../../doc/models/poi-software.md) | Required | Information related to the software of the POI System which manages the Sale to POI protocol. In a session allows identifying the product features of a POI System. |
| `poi_status` | [`POIStatus`](../../doc/models/poi-status.md) | Optional | Indicate the availability of the POI Terminal components. The data element is absent if the component is not part of the POI Terminal.<br>State of a POI Terminal. |

## Example

```python
import dateutil.parser

from adyen.models.global_status_1_enum import GlobalStatus1Enum
from adyen.models.poi_software import POISoftware
from adyen.models.poi_status import POIStatus
from adyen.models.poi_system_data_1 import POISystemData1
from adyen.models.printer_status_1_enum import PrinterStatus1Enum

poi_system_data_1 = POISystemData1(
    date_time=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    poi_software=POISoftware(
        manufacturer_id='ManufacturerID4',
        application_name='ApplicationName8',
        software_version='SoftwareVersion0',
        certification_code='CertificationCode4'
    ),
    poi_status=POIStatus(
        global_status=GlobalStatus1Enum.MAINTENANCE,
        security_ok_flag=False,
        pedok_flag=False,
        card_reader_ok_flag=False,
        printer_status=PrinterStatus1Enum.PAPERLOW,
        communication_ok_flag=False
    )
)
```

