
# Grant Offer 1

## Structure

`GrantOffer1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_holder_id` | `str` | Required | The unique identifier of the account holder to which the grant is offered. |
| `amount` | [`Amount17`](../../doc/models/amount-17.md) | Optional | The amount that would be paid out to the user for business financing. |
| `contract_type` | [`ContractTypeEnum`](../../doc/models/contract-type-enum.md) | Optional | The contract type of the offer.<br><br>Possible values:<br><br>* **loan**<br>* **cashAdvance** |
| `expires_at` | `datetime` | Optional | The expiration date and time of the offer validity period. |
| `fee` | [`GrantOfferFee1`](../../doc/models/grant-offer-fee-1.md) | Optional | Contains information about the fee that your user would pay for the grant. |
| `id` | `str` | Optional | The unique identifier of the offer. |
| `repayment` | [`Repayment11`](../../doc/models/repayment-11.md) | Optional | Contains information about the repayment configuration of the grant. |
| `starts_at` | `datetime` | Optional | The starting date and time of the offer validity period. |

## Example

```python
import dateutil.parser

from adyen.models.amount_17 import Amount17
from adyen.models.contract_type_enum import ContractTypeEnum
from adyen.models.grant_offer_1 import GrantOffer1
from adyen.models.grant_offer_fee_1 import GrantOfferFee1

grant_offer_1 = GrantOffer1(
    account_holder_id='accountHolderId8',
    amount=Amount17(
        currency='currency2',
        value=110
    ),
    contract_type=ContractTypeEnum.CASHADVANCE,
    expires_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    fee=GrantOfferFee1(
        amount=Amount17(
            currency='currency2',
            value=110
        ),
        apr_basis_points=142
    ),
    id='id6'
)
```

