
# Login Response

It conveys Information related to the Login to process.
Content of the Login Response message.

## Structure

`LoginResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `response` | [`Response11`](../../doc/models/response-11.md) | Required | Result of a message request processing. |
| `poi_system_data` | [`POISystemData1`](../../doc/models/poi-system-data-1.md) | Optional | Information related to the POI System.<br>Returned if the response result is Success. |
| `token_request_status` | `bool` | Optional | If token is managed by the POI, the status of the token request. |

## Example

```python
import dateutil.parser

from adyen.models.error_condition_1_enum import ErrorCondition1Enum
from adyen.models.global_status_1_enum import GlobalStatus1Enum
from adyen.models.login_response import LoginResponse
from adyen.models.poi_software import POISoftware
from adyen.models.poi_status import POIStatus
from adyen.models.poi_system_data_1 import POISystemData1
from adyen.models.printer_status_1_enum import PrinterStatus1Enum
from adyen.models.response_11 import Response11
from adyen.models.result_11_enum import Result11Enum

login_response = LoginResponse(
    response=Response11(
        result=Result11Enum.PARTIAL,
        error_condition=ErrorCondition1Enum.PAYMENTRESTRICTION,
        additional_response='AdditionalResponse8'
    ),
    poi_system_data=POISystemData1(
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
    ),
    token_request_status=False
)
```

