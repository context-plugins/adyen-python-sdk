
# Diagnosis Request 3

*This model accepts additional fields of type Any.*

## Structure

`DiagnosisRequest3`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `poiid` | `str` | Optional | Identification of a POI System or a POI Terminal for the Sale to POI protocol.<br>MessageHeader.POIID.<br><br>**Constraints**: *Pattern*: `^.+$` |
| `host_diagnosis_flag` | `bool` | Optional | Indicates if Host Diagnosis are required.<br><br>**Default**: `False` |
| `acquirer_id` | `List[int]` | Optional | Identification of the Acquirer.<br>Present if requesting the diagnosis of these hosts only. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.diagnosis_request_3 import DiagnosisRequest3

diagnosis_request_3 = DiagnosisRequest3(
    poiid='POIID6',
    host_diagnosis_flag=False,
    acquirer_id=[
        38
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

