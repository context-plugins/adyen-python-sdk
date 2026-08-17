
# Disbursements

## Structure

`Disbursements`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `disbursements` | [`List[Disbursement]`](../../doc/models/disbursement.md) | Required | Contains a list of all disbursements related to the specified grant. |

## Example

```python
from adyen.models.amount_17 import Amount17
from adyen.models.bank_account_identification_1 import BankAccountIdentification1
from adyen.models.capital_balance import CapitalBalance
from adyen.models.disbursement import Disbursement
from adyen.models.disbursement_repayment_2 import DisbursementRepayment2
from adyen.models.disbursements import Disbursements
from adyen.models.fee_22 import Fee22
from adyen.models.funds_collection import FundsCollection
from adyen.models.funds_collection_type_2_enum import FundsCollectionType2Enum

disbursements = Disbursements(
    disbursements=[
        Disbursement(
            account_holder_id='accountHolderId0',
            amount=Amount17(
                currency='currency2',
                value=110
            ),
            balance_account_id='balanceAccountId0',
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
            grant_id='grantId6',
            id='id8',
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
                ),
                FundsCollection(
                    account_identification=BankAccountIdentification1(
                        mtype='BankAccountIdentification1'
                    ),
                    funds_collection_type=FundsCollectionType2Enum.UNSCHEDULEDREPAYMENT
                )
            ]
        )
    ]
)
```

