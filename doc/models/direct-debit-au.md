
# Direct Debit Au

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
| `mtype` | [`Type22Enum`](../../doc/models/type-22-enum.md) | Optional | **directdebit_AU**<br><br>**Default**: `"directdebit_AU"` |

## Example

```python
from adyen.models.direct_debit_au import DirectDebitAu
from adyen.models.type_22_enum import Type22Enum

direct_debit_au = DirectDebitAu(
    holder_name='holderName2',
    bank_account_number='bankAccountNumber6',
    bank_branch_code='bankBranchCode6',
    checkout_attempt_id='checkoutAttemptId2',
    recurring_detail_reference='recurringDetailReference6',
    sdk_data='sdkData6',
    mtype=Type22Enum.DIRECTDEBIT_AU
)
```

