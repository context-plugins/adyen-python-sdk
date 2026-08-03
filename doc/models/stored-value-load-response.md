
# Stored Value Load Response

*This model accepts additional fields of type Any.*

## Structure

`StoredValueLoadResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `auth_code` | `str` | Optional | Authorisation code:<br><br>* When the payment is authorised, this field holds the authorisation code for the payment.<br>* When the payment is not authorised, this field is empty. |
| `current_balance` | [`CurrentBalance`](../../doc/models/current-balance.md) | Optional | - |
| `psp_reference` | `str` | Optional | Adyen's 16-character string reference associated with the transaction/request. This value is globally unique; quote it when communicating with us about this request. |
| `refusal_reason` | `str` | Optional | If the transaction is refused or an error occurs, this field holds Adyen's mapped reason for the refusal or a description of the error.<br><br>When a transaction fails, the authorisation response includes `resultCode` and `refusalReason` values. |
| `result_code` | [`ResultCode3`](../../doc/models/result-code-3.md) | Optional | - |
| `third_party_refusal_reason` | `str` | Optional | Raw refusal reason received from the third party, where available |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.current_balance import CurrentBalance
from adyen.models.result_code_3 import ResultCode3
from adyen.models.stored_value_load_response import StoredValueLoadResponse

stored_value_load_response = StoredValueLoadResponse(
    auth_code='authCode2',
    current_balance=CurrentBalance(
        currency='currency2',
        value=232,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    psp_reference='pspReference0',
    refusal_reason='refusalReason8',
    result_code=ResultCode3.ERROR,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

