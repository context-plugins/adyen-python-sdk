
# Calculated Grant Offer

## Structure

`CalculatedGrantOffer`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_holder_id` | `str` | Required | The unique identifier of the account holder that the dynamic offer is for. |
| `amount` | [`Amount17`](../../doc/models/amount-17.md) | Required | The financing amount that would be paid out to your user. |
| `contract_type` | [`ContractTypeEnum`](../../doc/models/contract-type-enum.md) | Required | The contract type of the offer.<br><br>Possible values:<br><br>* **loan**<br>* **cashAdvance** |
| `expires_at` | `datetime` | Required | The expiration date and time of the offer validity period. |
| `fee` | [`GrantOfferFee1`](../../doc/models/grant-offer-fee-1.md) | Required | Contains information about the fee that your user would pay for the grant. |
| `repayment` | [`Repayment11`](../../doc/models/repayment-11.md) | Required | Contains information about the repayment configuration of the grant. |
| `starts_at` | `datetime` | Required | The starting date and time of the offer validity period. |

## Example

```python
import dateutil.parser

from adyen.models.amount_17 import Amount17
from adyen.models.calculated_grant_offer import CalculatedGrantOffer
from adyen.models.contract_type_enum import ContractTypeEnum
from adyen.models.grant_offer_fee_1 import GrantOfferFee1
from adyen.models.repayment_11 import Repayment11
from adyen.models.repayment_term import RepaymentTerm
from adyen.models.threshold_repayment_21 import ThresholdRepayment21

calculated_grant_offer = CalculatedGrantOffer(
    account_holder_id='accountHolderId4',
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
    repayment=Repayment11(
        basis_points=18,
        term=RepaymentTerm(
            estimated_days=248,
            maximum_days=24
        ),
        threshold=ThresholdRepayment21(
            amount=Amount17(
                currency='currency2',
                value=110
            )
        )
    ),
    starts_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
)
```

