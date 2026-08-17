
# BACS Direct Debit

## Structure

`BACSDirectDebit`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `bank_account_number` | `str` | Optional | The bank account number (without separators). |
| `bank_location_id` | `str` | Optional | The bank routing number of the account. |
| `checkout_attempt_id` | `str` | Optional | The checkout attempt identifier. |
| `holder_name` | `str` | Optional | The name of the bank account holder. |
| `recurring_detail_reference` | `str` | Optional | This is the `recurringDetailReference` returned in the response when you created the token. |
| `sdk_data` | `str` | Optional | Base64-encoded JSON object containing SDK related parameters required by the SDK<br><br>**Constraints**: *Maximum Length*: `50000` |
| `stored_payment_method_id` | `str` | Optional | This is the `recurringDetailReference` returned in the response when you created the token.<br><br>**Constraints**: *Maximum Length*: `64` |
| `transfer_instrument_id` | `str` | Optional | The unique identifier of your user's verified transfer instrument, which you can use to top up their balance accounts. |
| `mtype` | [`Type10Enum`](../../doc/models/type-10-enum.md) | Optional | **directdebit_GB**<br><br>**Default**: `"directdebit_GB"` |

## Example

```python
from adyen.models.bacs_direct_debit import BACSDirectDebit
from adyen.models.type_10_enum import Type10Enum

bacs_direct_debit = BACSDirectDebit(
    bank_account_number='bankAccountNumber2',
    bank_location_id='bankLocationId6',
    checkout_attempt_id='checkoutAttemptId8',
    holder_name='holderName8',
    recurring_detail_reference='recurringDetailReference2',
    mtype=Type10Enum.DIRECTDEBIT_GB
)
```

