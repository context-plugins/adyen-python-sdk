
# Sepa Direct Debit

*This model accepts additional fields of type Any.*

## Structure

`SepaDirectDebit`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `checkout_attempt_id` | `str` | Optional | The checkout attempt identifier. |
| `due_date` | `str` | Optional | The date that the the shopper's bank account is charged. |
| `iban` | `str` | Required | The International Bank Account Number (IBAN). |
| `owner_name` | `str` | Required | The name of the bank account holder. |
| `recurring_detail_reference` | `str` | Optional | This is the `recurringDetailReference` returned in the response when you created the token. |
| `sdk_data` | `str` | Optional | Base64-encoded JSON object containing SDK related parameters required by the SDK<br><br>**Constraints**: *Maximum Length*: `50000` |
| `stored_payment_method_id` | `str` | Optional | This is the `recurringDetailReference` returned in the response when you created the token.<br><br>**Constraints**: *Maximum Length*: `64` |
| `transfer_instrument_id` | `str` | Optional | The unique identifier of your user's verified transfer instrument, which you can use to top up their balance accounts. |
| `mtype` | [`Type511`](../../doc/models/type-511.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.sepa_direct_debit import SepaDirectDebit

sepa_direct_debit = SepaDirectDebit(
    iban='iban6',
    owner_name='ownerName6',
    checkout_attempt_id='checkoutAttemptId8',
    due_date='dueDate8',
    recurring_detail_reference='recurringDetailReference2',
    sdk_data='sdkData8',
    stored_payment_method_id='storedPaymentMethodId6',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

