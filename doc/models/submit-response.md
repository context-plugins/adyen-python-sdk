
# Submit Response

*This model accepts additional fields of type Any.*

## Structure

`SubmitResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `additional_data` | `Dict[str, str]` | Optional | This field contains additional data, which may be returned in a particular response. |
| `psp_reference` | `str` | Required | A new reference to uniquely identify this request. |
| `refusal_reason` | `str` | Optional | In case of refusal, an informational message for the reason. |
| `result_code` | `str` | Required | The response:<br><br>* In case of success, it is `payout-submit-received`.<br>* In case of an error, an informational message is returned. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.submit_response import SubmitResponse

submit_response = SubmitResponse(
    psp_reference='pspReference0',
    result_code='resultCode6',
    additional_data={
        'key0': 'additionalData8',
        'key1': 'additionalData9',
        'key2': 'additionalData0'
    },
    refusal_reason='refusalReason2',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

