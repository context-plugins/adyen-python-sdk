
# Disbursement

*This model accepts additional fields of type Any.*

## Structure

`Disbursement`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_holder_id` | `str` | Required | The unique identifier of the account holder that received the disbursement. |
| `amount` | [`Amount5`](../../doc/models/amount-5.md) | Required | - |
| `balance_account_id` | `str` | Required | The unique identifier of the balance account that received the disbursement. |
| `balances` | [`Balances`](../../doc/models/balances.md) | Required | - |
| `fee` | [`Fee2`](../../doc/models/fee-2.md) | Required | - |
| `funds_collections` | [`List[FundsCollection]`](../../doc/models/funds-collection.md) | Optional | Contains information about the accounts that Adyen uses to collect funds related to repayments. |
| `grant_id` | `str` | Required | The unique identifier of the grant related to the disbursement. |
| `id` | `str` | Required | The unique identifier of the disbursement. |
| `repayment` | [`DisbursementRepayment`](../../doc/models/disbursement-repayment.md) | Required | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.amount_5 import Amount5
from adyen.models.balances import Balances
from adyen.models.bank_account_identification_1 import BankAccountIdentification1
from adyen.models.disbursement import Disbursement
from adyen.models.disbursement_repayment import DisbursementRepayment
from adyen.models.fee_2 import Fee2
from adyen.models.funds_collection import FundsCollection
from adyen.models.funds_collection_type_2 import FundsCollectionType2

disbursement = Disbursement(
    account_holder_id='accountHolderId2',
    amount=Amount5(
        currency='currency2',
        value=110,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    balance_account_id='balanceAccountId2',
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
    grant_id='grantId8',
    id='id0',
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
        )
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

