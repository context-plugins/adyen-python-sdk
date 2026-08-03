
# Response Additional Data Sepa

*This model accepts additional fields of type Any.*

## Structure

`ResponseAdditionalDataSepa`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `sepadirectdebit_date_of_signature` | `str` | Optional | The transaction signature date.<br><br>Format: yyyy-MM-dd |
| `sepadirectdebit_mandate_id` | `str` | Optional | Its value corresponds to the pspReference value of the transaction. |
| `sepadirectdebit_sepadirectdebit_due_date` | `str` | Optional | The date that the the shopper's bank account is charged. |
| `sepadirectdebit_sequence_type` | `str` | Optional | This field can take one of the following values:<br><br>* OneOff: (OOFF) Direct debit instruction to initiate exactly one direct debit transaction.<br><br>* First: (FRST) Initial/first collection in a series of direct debit instructions.<br><br>* Recurring: (RCUR) Direct debit instruction to carry out regular direct debit transactions initiated by the creditor.<br><br>* Final: (FNAL) Last/final collection in a series of direct debit instructions.<br><br>Example: OOFF |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.response_additional_data_sepa import ResponseAdditionalDataSepa

response_additional_data_sepa = ResponseAdditionalDataSepa(
    sepadirectdebit_date_of_signature='sepadirectdebit.dateOfSignature8',
    sepadirectdebit_mandate_id='sepadirectdebit.mandateId2',
    sepadirectdebit_sepadirectdebit_due_date='sepadirectdebit.sepadirectdebit.dueDate6',
    sepadirectdebit_sequence_type='sepadirectdebit.sequenceType0',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

