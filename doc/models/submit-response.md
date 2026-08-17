
# Submit Response

## Structure

`SubmitResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `additional_data` | `Dict[str, str]` | Optional | This field contains additional data, which may be returned in a particular response. |
| `psp_reference` | `str` | Required | A new reference to uniquely identify this request. |
| `refusal_reason` | `str` | Optional | In case of refusal, an informational message for the reason. |
| `result_code` | `str` | Required | The response:<br><br>* In case of success, it is `payout-submit-received`.<br>* In case of an error, an informational message is returned. |

## Example

```python
from adyen.models.submit_response import SubmitResponse

submit_response = SubmitResponse(
    psp_reference='pspReference0',
    result_code='resultCode6',
    additional_data={
        'key0': 'additionalData8',
        'key1': 'additionalData9',
        'key2': 'additionalData0'
    },
    refusal_reason='refusalReason2'
)
```

