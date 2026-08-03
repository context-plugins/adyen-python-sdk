
# Funding Instrument

*This model accepts additional fields of type Any.*

## Structure

`FundingInstrument`

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
from adyen.models.funding_instrument import FundingInstrument
from adyen.models.source_of_funds_2 import SourceOfFunds2

funding_instrument = FundingInstrument(
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
    network_payment_reference='networkPaymentReference4',
    reference='reference0',
    source_of_funds=SourceOfFunds2.DEBIT,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

