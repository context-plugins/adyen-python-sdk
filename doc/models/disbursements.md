
# Disbursements

*This model accepts additional fields of type Any.*

## Structure

`Disbursements`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `disbursements` | [`List[Disbursement]`](../../doc/models/disbursement.md) | Required | Contains a list of all disbursements related to the specified grant. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.amount_5 import Amount5
from adyen.models.balances import Balances
from adyen.models.bank_account_identification_1 import BankAccountIdentification1
from adyen.models.disbursement import Disbursement
from adyen.models.disbursement_repayment import DisbursementRepayment
from adyen.models.disbursements import Disbursements
from adyen.models.fee_2 import Fee2
from adyen.models.funds_collection import FundsCollection
from adyen.models.funds_collection_type_2 import FundsCollectionType2

disbursements = Disbursements(
    disbursements=[
        Disbursement(
            account_holder_id='accountHolderId0',
            amount=Amount5(
                currency='currency2',
                value=110,
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            balance_account_id='balanceAccountId0',
            balances=Balances(
                currency='currency0',
                fee=72,
                principal=110,
                total=150,
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            fee=Fee2(
                amount=Amount5(
                    currency='currency2',
                    value=110,
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                ),
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            grant_id='grantId6',
            id='id8',
            repayment=DisbursementRepayment(
                basis_points=18,
                update_description='updateDescription0',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            funds_collections=[
                FundsCollection(
                    account_identification=BankAccountIdentification1(
                        mtype='BankAccountIdentification1',
                        additional_properties={
                            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                        }
                    ),
                    funds_collection_type=FundsCollectionType2.UNSCHEDULEDREPAYMENT,
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                ),
                FundsCollection(
                    account_identification=BankAccountIdentification1(
                        mtype='BankAccountIdentification1',
                        additional_properties={
                            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                        }
                    ),
                    funds_collection_type=FundsCollectionType2.UNSCHEDULEDREPAYMENT,
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                )
            ],
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

