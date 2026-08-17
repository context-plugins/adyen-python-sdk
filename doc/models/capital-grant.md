
# Capital Grant

## Structure

`CapitalGrant`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amount` | [`Amount17`](../../doc/models/amount-17.md) | Optional | An object containing the amount of the grant, in [minor units](https://docs.adyen.com/development-resources/currency-codes). |
| `balances` | [`CapitalBalance`](../../doc/models/capital-balance.md) | Required | An object containing the details of the existing grant. |
| `counterparty` | [`GrantCounterparty2`](../../doc/models/grant-counterparty-2.md) | Optional | An object containing the details of the receiving party of the grant. |
| `fee` | [`Fee4`](../../doc/models/fee-4.md) | Optional | An object containing the fee currency and value, in [minor units](https://docs.adyen.com/development-resources/currency-codes). |
| `grant_account_id` | `str` | Required | The identifier of the grant account used for the grant. |
| `grant_offer_id` | `str` | Required | The identifier of the grant offer that has been selected and from which the grant details will be used. |
| `id` | `str` | Required | The identifier of the grant reference. |
| `repayment` | [`Repayment`](../../doc/models/repayment.md) | Optional | An object containing the details of the 30-day repayment threshold. |
| `status` | [`Status14Enum`](../../doc/models/status-14-enum.md) | Required | The current status of the grant. Possible values: **Pending**, **Active**, **Repaid**, **WrittenOff**, **Failed**, **Revoked**. |

## Example

```python
from adyen.models.amount_17 import Amount17
from adyen.models.capital_balance import CapitalBalance
from adyen.models.capital_grant import CapitalGrant
from adyen.models.fee_4 import Fee4
from adyen.models.grant_counterparty_2 import GrantCounterparty2
from adyen.models.repayment import Repayment
from adyen.models.repayment_term import RepaymentTerm
from adyen.models.status_14_enum import Status14Enum
from adyen.models.threshold_repayment_2 import ThresholdRepayment2

capital_grant = CapitalGrant(
    balances=CapitalBalance(
        currency='currency0',
        fee=72,
        principal=110,
        total=150
    ),
    grant_account_id='grantAccountId4',
    grant_offer_id='grantOfferId8',
    id='id8',
    status=Status14Enum.REPAID,
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
```

