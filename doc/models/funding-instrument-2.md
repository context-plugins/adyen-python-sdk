
# Funding Instrument 2

Details of the card or token used to fund the pay-in transaction.

## Structure

`FundingInstrument2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `card_identification` | [`CardIdentification2`](../../doc/models/card-identification-2.md) | Optional | Card details used for the transfer, such as the Primary Account Number (PAN) or stored payment method ID. Required if `sourceOfFunds` is **DEBIT**. Provide either:<br><br>- `storedPaymentMethodId` or<br>- `expiryMonth`, `expiryYear`, and `number`. |
| `network_payment_reference` | `str` | Optional | The unique reference assigned by the card network for the pay-in transaction. |
| `reference` | `str` | Optional | Your internal reference that identifies this funding instrument. Required if `sourceOfFunds` is **DEPOSIT_ACCOUNT**. |
| `source_of_funds` | [`SourceOfFundsEnum`](../../doc/models/source-of-funds-enum.md) | Optional | Indicates where the funds used for the transfer originated. Possible values are:<br><br>- **DEBIT** for card-to-card transfers.<br>- **DEPOSIT_ACCOUNT** for wallet-to-card transfers. |

## Example

```python
from adyen.models.card_identification_2 import CardIdentification2
from adyen.models.funding_instrument_2 import FundingInstrument2
from adyen.models.source_of_funds_enum import SourceOfFundsEnum

funding_instrument_2 = FundingInstrument2(
    card_identification=CardIdentification2(
        expiry_month='expiryMonth2',
        expiry_year='expiryYear2',
        issue_number='issueNumber0',
        number='number6',
        start_month='startMonth8'
    ),
    network_payment_reference='networkPaymentReference6',
    reference='reference8',
    source_of_funds=SourceOfFundsEnum.DEBIT
)
```

