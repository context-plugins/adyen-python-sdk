
# Find Transfers Response

*This model accepts additional fields of type Any.*

## Structure

`FindTransfersResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `links` | [`Links3`](../../doc/models/links-3.md) | Optional | - |
| `data` | [`List[TransferData]`](../../doc/models/transfer-data.md) | Optional | Contains the transfers that match the query parameters. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.amount_5 import Amount5
from adyen.models.balance_mutation import BalanceMutation
from adyen.models.bank_category_data import BankCategoryData
from adyen.models.category_3 import Category3
from adyen.models.find_transfers_response import FindTransfersResponse
from adyen.models.links_3 import Links3
from adyen.models.next import Next
from adyen.models.prev import Prev
from adyen.models.priority import Priority
from adyen.models.resource_reference import ResourceReference
from adyen.models.status_53 import Status53
from adyen.models.transfer_data import TransferData
from adyen.models.type_312 import Type312

find_transfers_response = FindTransfersResponse(
    links=Links3(
        next=Next(
            href='href4',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        prev=Prev(
            href='href8',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    data=[
        TransferData(
            amount=Amount5(
                currency='currency2',
                value=110,
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            category=Category3.INTERNAL,
            status=Status53.CANCELLED,
            account_holder=ResourceReference(
                description='description0',
                id='id0',
                reference='reference4',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            balance_account=ResourceReference(
                description='description2',
                id='id2',
                reference='reference2',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            balance_platform='balancePlatform2',
            balances=[
                BalanceMutation(
                    balance=224,
                    currency='currency0',
                    received=214,
                    reserved=158,
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                ),
                BalanceMutation(
                    balance=224,
                    currency='currency0',
                    received=214,
                    reserved=158,
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                ),
                BalanceMutation(
                    balance=224,
                    currency='currency0',
                    received=214,
                    reserved=158,
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                )
            ],
            category_data=BankCategoryData(
                priority=Priority.INSTANT,
                mtype=Type312.BANK,
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        TransferData(
            amount=Amount5(
                currency='currency2',
                value=110,
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            category=Category3.INTERNAL,
            status=Status53.CANCELLED,
            account_holder=ResourceReference(
                description='description0',
                id='id0',
                reference='reference4',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            balance_account=ResourceReference(
                description='description2',
                id='id2',
                reference='reference2',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            balance_platform='balancePlatform2',
            balances=[
                BalanceMutation(
                    balance=224,
                    currency='currency0',
                    received=214,
                    reserved=158,
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                ),
                BalanceMutation(
                    balance=224,
                    currency='currency0',
                    received=214,
                    reserved=158,
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                ),
                BalanceMutation(
                    balance=224,
                    currency='currency0',
                    received=214,
                    reserved=158,
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                )
            ],
            category_data=BankCategoryData(
                priority=Priority.INSTANT,
                mtype=Type312.BANK,
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
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

