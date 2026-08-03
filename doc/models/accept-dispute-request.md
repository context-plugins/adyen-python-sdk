
# Accept Dispute Request

*This model accepts additional fields of type Any.*

## Structure

`AcceptDisputeRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `dispute_psp_reference` | `str` | Required | The PSP reference assigned to the dispute. |
| `merchant_account_code` | `str` | Required | The merchant account identifier, for which you want to process the dispute transaction. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.accept_dispute_request import AcceptDisputeRequest

accept_dispute_request = AcceptDisputeRequest(
    dispute_psp_reference='disputePspReference6',
    merchant_account_code='merchantAccountCode8',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

