
# Diagnosis Response

It conveys the result of the requested diagnosis and a possible message to display on a logical device.
Content of the Diagnosis Response message.

*This model accepts additional fields of type Any.*

## Structure

`DiagnosisResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `response` | [`Response3`](../../doc/models/response-3.md) | Required | - |
| `poi_status` | [`PoiStatus2`](../../doc/models/poi-status-2.md) | Optional | - |
| `host_status` | [`List[HostStatus]`](../../doc/models/host-status.md) | Optional | State of a Host. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.diagnosis_response import DiagnosisResponse
from adyen.models.error_condition_1 import ErrorCondition1
from adyen.models.global_status_1 import GlobalStatus1
from adyen.models.host_status import HostStatus
from adyen.models.poi_status_2 import PoiStatus2
from adyen.models.printer_status_1 import PrinterStatus1
from adyen.models.response_3 import Response3
from adyen.models.result_11 import Result11

diagnosis_response = DiagnosisResponse(
    response=Response3(
        result=Result11.PARTIAL,
        error_condition=ErrorCondition1.PAYMENTRESTRICTION,
        additional_response='AdditionalResponse8',
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
    host_status=[
        HostStatus(
            acquirer_id=120,
            is_reachable_flag=False,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        HostStatus(
            acquirer_id=120,
            is_reachable_flag=False,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        HostStatus(
            acquirer_id=120,
            is_reachable_flag=False,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

