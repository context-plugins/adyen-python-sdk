
# Bacs Direct Debit

*This model accepts additional fields of type Any.*

## Structure

`BacsDirectDebit`

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
| `mtype` | [`Type101`](../../doc/models/type-101.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.bacs_direct_debit import BacsDirectDebit

bacs_direct_debit = BacsDirectDebit(
    bank_account_number='bankAccountNumber2',
    bank_location_id='bankLocationId6',
    checkout_attempt_id='checkoutAttemptId8',
    holder_name='holderName8',
    recurring_detail_reference='recurringDetailReference2',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

