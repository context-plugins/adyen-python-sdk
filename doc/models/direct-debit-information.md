
# Direct Debit Information

## Structure

`DirectDebitInformation`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `date_of_signature` | `datetime` | Optional | The date when the direct debit mandate was accepted by your user, in [ISO-8601](https://www.w3.org/TR/NOTE-datetime) format. |
| `due_date` | `datetime` | Optional | The date when the funds are deducted from your user's balance account. |
| `mandate_id` | `str` | Optional | Your unique identifier for the direct debit mandate. |
| `sequence_type` | `str` | Optional | Identifies the direct debit transfer's type.<br>Possible values: **OneOff**, **First**, **Recurring**, **Final**. |

## Example

```python
import dateutil.parser

from adyen.models.direct_debit_information import DirectDebitInformation

direct_debit_information = DirectDebitInformation(
    date_of_signature=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    due_date=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    mandate_id='mandateId6',
    sequence_type='sequenceType4'
)
```

