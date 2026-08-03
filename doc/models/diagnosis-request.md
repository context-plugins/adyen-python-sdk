
# Diagnosis Request

It conveys Information related to the target POI for which the diagnosis is requested.
Content of the Diagnosis Request message.

*This model accepts additional fields of type Any.*

## Structure

`DiagnosisRequest`

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

from adyen.models.diagnosis_request import DiagnosisRequest

diagnosis_request = DiagnosisRequest(
    poiid='POIID2',
    host_diagnosis_flag=False,
    acquirer_id=[
        72,
        73,
        74
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

