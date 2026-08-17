
# Capital Grants

## Structure

`CapitalGrants`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `grants` | [`List[CapitalGrant]`](../../doc/models/capital-grant.md) | Required | The unique identifier of the grant. |

## Example

```python
from adyen.models.amount_17 import Amount17
from adyen.models.capital_balance import CapitalBalance
from adyen.models.capital_grant import CapitalGrant
from adyen.models.capital_grants import CapitalGrants
from adyen.models.fee_4 import Fee4
from adyen.models.grant_counterparty_2 import GrantCounterparty2
from adyen.models.repayment import Repayment
from adyen.models.repayment_term import RepaymentTerm
from adyen.models.status_14_enum import Status14Enum
from adyen.models.threshold_repayment_2 import ThresholdRepayment2

capital_grants = CapitalGrants(
    grants=[
        CapitalGrant(
            balances=CapitalBalance(
                currency='currency0',
                fee=72,
                principal=110,
                total=150
            ),
            grant_account_id='grantAccountId6',
            grant_offer_id='grantOfferId6',
            id='id0',
            status=Status14Enum.PENDING,
            amount=Amount17(
                currency='currency2',
                value=110
            ),
            counterparty=GrantCounterparty2(
                account_holder_id='accountHolderId0',
                balance_account_id='balanceAccountId0',
                transfer_instrument_id='transferInstrumentId4'
            ),
            fee=Fee4(
                amount=Amount17(
                    currency='currency2',
                    value=110
                )
            ),
            repayment=Repayment(
                basis_points=18,
                term=RepaymentTerm(
                    estimated_days=248,
                    maximum_days=24
                ),
                threshold=ThresholdRepayment2(
                    amount=Amount17(
                        currency='currency2',
                        value=110
                    )
                )
            )
        )
    ]
)
```

