
# Stored Value Balance Check Response

## Structure

`StoredValueBalanceCheckResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `current_balance` | [`Amount`](../../doc/models/amount.md) | Optional | The balance currently on the payment method. |
| `psp_reference` | `str` | Optional | Adyen's 16-character string reference associated with the transaction/request. This value is globally unique; quote it when communicating with us about this request. |
| `refusal_reason` | `str` | Optional | If the transaction is refused or an error occurs, this field holds Adyen's mapped reason for the refusal or a description of the error.<br><br>When a transaction fails, the authorisation response includes `resultCode` and `refusalReason` values. |
| `result_code` | [`ResultCode3Enum`](../../doc/models/result-code-3-enum.md) | Optional | The result of the payment. Possible values:<br><br>* **Success** – The operation has been completed successfully.<br>* **Refused** – The operation was refused. The reason is given in the `refusalReason` field.<br>* **Error** – There was an error when the operation was processed. The reason is given in the `refusalReason` field.<br>* **NotEnoughBalance** – The amount on the payment method is lower than the amount given in the request. Only applicable to balance checks. |
| `third_party_refusal_reason` | `str` | Optional | Raw refusal reason received from the third party, where available |

## Example

```python
from adyen.models.amount import Amount
from adyen.models.result_code_3_enum import ResultCode3Enum
from adyen.models.stored_value_balance_check_response import StoredValueBalanceCheckResponse

stored_value_balance_check_response = StoredValueBalanceCheckResponse(
    current_balance=Amount(
        currency='currency2',
        value=232
    ),
    psp_reference='pspReference8',
    refusal_reason='refusalReason6',
    result_code=ResultCode3Enum.ERROR,
    third_party_refusal_reason='thirdPartyRefusalReason8'
)
```

