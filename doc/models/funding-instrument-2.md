
# Funding Instrument 2

Details of the card or token used to fund the pay-in transaction.

*This model accepts additional fields of type Any.*

## Structure

`FundingInstrument2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `card_identification` | [`CardIdentification`](../../doc/models/card-identification.md) | Optional | - |
| `network_payment_reference` | `str` | Optional | The unique reference assigned by the card network for the pay-in transaction. |
| `reference` | `str` | Optional | Your internal reference that identifies this funding instrument. Required if `sourceOfFunds` is **DEPOSIT_ACCOUNT**. |
| `source_of_funds` | [`SourceOfFunds2`](../../doc/models/source-of-funds-2.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.card_identification import CardIdentification
from adyen.models.funding_instrument_2 import FundingInstrument2
from adyen.models.source_of_funds_2 import SourceOfFunds2

funding_instrument_2 = FundingInstrument2(
    card_identification=CardIdentification(
        expiry_month='expiryMonth2',
        expiry_year='expiryYear2',
        issue_number='issueNumber0',
        number='number6',
        start_month='startMonth8',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    network_payment_reference='networkPaymentReference6',
    reference='reference8',
    source_of_funds=SourceOfFunds2.DEBIT,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

