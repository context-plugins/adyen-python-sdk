
# Disbursement

## Structure

`Disbursement`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_holder_id` | `str` | Required | The unique identifier of the account holder that received the disbursement. |
| `amount` | [`Amount17`](../../doc/models/amount-17.md) | Required | Contains information about the amount of the disbursement. |
| `balance_account_id` | `str` | Required | The unique identifier of the balance account that received the disbursement. |
| `balances` | [`CapitalBalance`](../../doc/models/capital-balance.md) | Required | Contains information about the balances of the disbursement. |
| `fee` | [`Fee22`](../../doc/models/fee-22.md) | Required | Contains information about the fee that your user must pay for the disbursement. |
| `funds_collections` | [`List[FundsCollection]`](../../doc/models/funds-collection.md) | Optional | Contains information about the accounts that Adyen uses to collect funds related to repayments. |
| `grant_id` | `str` | Required | The unique identifier of the grant related to the disbursement. |
| `id` | `str` | Required | The unique identifier of the disbursement. |
| `repayment` | [`DisbursementRepayment2`](../../doc/models/disbursement-repayment-2.md) | Required | Contains information about the basis points configured for repaying the disbursement. |

## Example

```python
from adyen.models.amount_17 import Amount17
from adyen.models.bank_account_identification_1 import BankAccountIdentification1
from adyen.models.capital_balance import CapitalBalance
from adyen.models.disbursement import Disbursement
from adyen.models.disbursement_repayment_2 import DisbursementRepayment2
from adyen.models.fee_22 import Fee22
from adyen.models.funds_collection import FundsCollection
from adyen.models.funds_collection_type_2_enum import FundsCollectionType2Enum

disbursement = Disbursement(
    account_holder_id='accountHolderId2',
    amount=Amount17(
        currency='currency2',
        value=110
    ),
    balance_account_id='balanceAccountId2',
    balances=CapitalBalance(
        currency='currency0',
        fee=72,
        principal=110,
        total=150
    ),
    fee=Fee22(
        amount=Amount17(
            currency='currency2',
            value=110
        )
    ),
    grant_id='grantId8',
    id='id0',
    repayment=DisbursementRepayment2(
        basis_points=18,
        update_description='updateDescription0'
    ),
    funds_collections=[
        FundsCollection(
            account_identification=BankAccountIdentification1(
                mtype='BankAccountIdentification1'
            ),
            funds_collection_type=FundsCollectionType2Enum.UNSCHEDULEDREPAYMENT
        )
    ]
)
```

