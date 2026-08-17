
# Diagnosis Request 2

Content of the Diagnosis Request message.

## Structure

`DiagnosisRequest2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `poiid` | `str` | Optional | Identification of a POI System or a POI Terminal for the Sale to POI protocol.<br>MessageHeader.POIID.<br><br>**Constraints**: *Pattern*: `^.+$` |
| `host_diagnosis_flag` | `bool` | Optional | Indicates if Host Diagnosis are required.<br><br>**Default**: `False` |
| `acquirer_id` | `List[int]` | Optional | Identification of the Acquirer.<br>Present if requesting the diagnosis of these hosts only. |

## Example

```python
from adyen.models.diagnosis_request_2 import DiagnosisRequest2

diagnosis_request_2 = DiagnosisRequest2(
    poiid='POIID8',
    host_diagnosis_flag=False,
    acquirer_id=[
        240,
        241
    ]
)
```

