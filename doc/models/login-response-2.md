
# Login Response 2

Content of the Login Response message.

*This model accepts additional fields of type Any.*

## Structure

`LoginResponse2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `response` | [`Response3`](../../doc/models/response-3.md) | Required | - |
| `poi_system_data` | [`PoiSystemData`](../../doc/models/poi-system-data.md) | Optional | - |
| `token_request_status` | `bool` | Optional | If token is managed by the POI, the status of the token request. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from adyen.models.error_condition_1 import ErrorCondition1
from adyen.models.global_status_1 import GlobalStatus1
from adyen.models.login_response_2 import LoginResponse2
from adyen.models.poi_software_1 import PoiSoftware1
from adyen.models.poi_status_2 import PoiStatus2
from adyen.models.poi_system_data import PoiSystemData
from adyen.models.printer_status_1 import PrinterStatus1
from adyen.models.response_3 import Response3
from adyen.models.result_11 import Result11

login_response_2 = LoginResponse2(
    response=Response3(
        result=Result11.PARTIAL,
        error_condition=ErrorCondition1.PAYMENTRESTRICTION,
        additional_response='AdditionalResponse8',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    poi_system_data=PoiSystemData(
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
    ),
    token_request_status=False,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

