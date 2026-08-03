
# Store Detail and Submit Response

*This model accepts additional fields of type Any.*

## Structure

`StoreDetailAndSubmitResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `additional_data` | `Dict[str, str]` | Optional | This field contains additional data, which may be returned in a particular response. |
| `psp_reference` | `str` | Required | A new reference to uniquely identify this request. |
| `refusal_reason` | `str` | Optional | In case of refusal, an informational message for the reason. |
| `result_code` | `str` | Required | The response:<br><br>* In case of success is payout-submit-received.<br>* In case of an error, an informational message is returned. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.store_detail_and_submit_response import StoreDetailAndSubmitResponse

store_detail_and_submit_response = StoreDetailAndSubmitResponse(
    psp_reference='pspReference8',
    result_code='resultCode4',
    additional_data={
        'key0': 'additionalData0',
        'key1': 'additionalData1',
        'key2': 'additionalData2'
    },
    refusal_reason='refusalReason0',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

