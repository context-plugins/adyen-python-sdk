
# Diagnosis Response

It conveys the result of the requested diagnosis and a possible message to display on a logical device.
Content of the Diagnosis Response message.

## Structure

`DiagnosisResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `response` | [`Response11`](../../doc/models/response-11.md) | Required | Result of a message request processing. |
| `poi_status` | [`POIStatus1`](../../doc/models/poi-status-1.md) | Optional | State of a POI Terminal.<br>If `Response.Result` is Success. |
| `host_status` | [`List[HostStatus]`](../../doc/models/host-status.md) | Optional | State of a Host. |

## Example

```python
from adyen.models.diagnosis_response import DiagnosisResponse
from adyen.models.error_condition_1_enum import ErrorCondition1Enum
from adyen.models.global_status_1_enum import GlobalStatus1Enum
from adyen.models.host_status import HostStatus
from adyen.models.poi_status_1 import POIStatus1
from adyen.models.printer_status_1_enum import PrinterStatus1Enum
from adyen.models.response_11 import Response11
from adyen.models.result_11_enum import Result11Enum

diagnosis_response = DiagnosisResponse(
    response=Response11(
        result=Result11Enum.PARTIAL,
        error_condition=ErrorCondition1Enum.PAYMENTRESTRICTION,
        additional_response='AdditionalResponse8'
    ),
    poi_status=POIStatus1(
        global_status=GlobalStatus1Enum.MAINTENANCE,
        security_ok_flag=False,
        pedok_flag=False,
        card_reader_ok_flag=False,
        printer_status=PrinterStatus1Enum.PAPERLOW,
        communication_ok_flag=False
    ),
    host_status=[
        HostStatus(
            acquirer_id=120,
            is_reachable_flag=False
        ),
        HostStatus(
            acquirer_id=120,
            is_reachable_flag=False
        ),
        HostStatus(
            acquirer_id=120,
            is_reachable_flag=False
        )
    ]
)
```

