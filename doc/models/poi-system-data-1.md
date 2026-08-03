
# Poi System Data 1

Information related to the POI System.
Returned if the response result is Success.

*This model accepts additional fields of type Any.*

## Structure

`PoiSystemData1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `date_time` | `datetime` | Required | Date and Time. In the response, the POI System gives its date and time to the Sale System. |
| `poi_software` | [`PoiSoftware1`](../../doc/models/poi-software-1.md) | Required | - |
| `poi_status` | [`PoiStatus2`](../../doc/models/poi-status-2.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from adyen.models.global_status_1 import GlobalStatus1
from adyen.models.poi_software_1 import PoiSoftware1
from adyen.models.poi_status_2 import PoiStatus2
from adyen.models.poi_system_data_1 import PoiSystemData1
from adyen.models.printer_status_1 import PrinterStatus1

poi_system_data_1 = PoiSystemData1(
    date_time=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    poi_software=PoiSoftware1(
        manufacturer_id='ManufacturerID4',
        application_name='ApplicationName8',
        software_version='SoftwareVersion0',
        certification_code='CertificationCode4',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    poi_status=PoiStatus2(
        global_status=GlobalStatus1.MAINTENANCE,
        security_ok_flag=False,
        pedok_flag=False,
        card_reader_ok_flag=False,
        printer_status=PrinterStatus1.PAPERLOW,
        communication_ok_flag=False,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

