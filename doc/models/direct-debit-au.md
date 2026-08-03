
# Direct Debit Au

*This model accepts additional fields of type Any.*

## Structure

`DirectDebitAu`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `bank_account_number` | `str` | Optional | The shopper's banking account number used to complete payment. |
| `bank_branch_code` | `str` | Optional | The shopper's BSB (their bank's branch code) number used to complete payment. |
| `checkout_attempt_id` | `str` | Optional | The checkout attempt identifier. |
| `holder_name` | `str` | Required | The name of the bank account holder. |
| `recurring_detail_reference` | `str` | Optional | This is the `recurringDetailReference` returned in the response when you created the token. |
| `sdk_data` | `str` | Optional | Base64-encoded JSON object containing SDK related parameters required by the SDK<br><br>**Constraints**: *Maximum Length*: `50000` |
| `stored_payment_method_id` | `str` | Optional | This is the `recurringDetailReference` returned in the response when you created the token.<br><br>**Constraints**: *Maximum Length*: `64` |
| `mtype` | [`Type221`](../../doc/models/type-221.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.direct_debit_au import DirectDebitAu

direct_debit_au = DirectDebitAu(
    holder_name='holderName2',
    bank_account_number='bankAccountNumber6',
    bank_branch_code='bankBranchCode6',
    checkout_attempt_id='checkoutAttemptId2',
    recurring_detail_reference='recurringDetailReference6',
    sdk_data='sdkData6',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

