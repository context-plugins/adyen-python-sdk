
# Find Transfers Response

## Structure

`FindTransfersResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `links` | [`Links21`](../../doc/models/links-21.md) | Optional | Contains links to the next and previous page whenever applicable. |
| `data` | [`List[TransferData]`](../../doc/models/transfer-data.md) | Optional | Contains the transfers that match the query parameters. |

## Example

```python
from adyen.models.amount_17 import Amount17
from adyen.models.balance_mutation import BalanceMutation
from adyen.models.bank_category_data import BankCategoryData
from adyen.models.category_3_enum import Category3Enum
from adyen.models.find_transfers_response import FindTransfersResponse
from adyen.models.links_21 import Links21
from adyen.models.links_element import LinksElement
from adyen.models.priority_1_enum import Priority1Enum
from adyen.models.resource_reference_1 import ResourceReference1
from adyen.models.resource_reference_5 import ResourceReference5
from adyen.models.status_51_enum import Status51Enum
from adyen.models.transfer_data import TransferData
from adyen.models.type_310_enum import Type310Enum

find_transfers_response = FindTransfersResponse(
    links=Links21(
        next=LinksElement(
            href='href4'
        ),
        prev=LinksElement(
            href='href8'
        )
    ),
    data=[
        TransferData(
            amount=Amount17(
                currency='currency2',
                value=110
            ),
            category=Category3Enum.INTERNAL,
            status=Status51Enum.CANCELLED,
            account_holder=ResourceReference5(
                description='description0',
                id='id0',
                reference='reference4'
            ),
            balance_account=ResourceReference1(
                description='description2',
                id='id2',
                reference='reference2'
            ),
            balance_platform='balancePlatform2',
            balances=[
                BalanceMutation(
                    balance=224,
                    currency='currency0',
                    received=214,
                    reserved=158
                ),
                BalanceMutation(
                    balance=224,
                    currency='currency0',
                    received=214,
                    reserved=158
                ),
                BalanceMutation(
                    balance=224,
                    currency='currency0',
                    received=214,
                    reserved=158
                )
            ],
            category_data=BankCategoryData(
                priority=Priority1Enum.INSTANT,
                mtype=Type310Enum.BANK
            )
        ),
        TransferData(
            amount=Amount17(
                currency='currency2',
                value=110
            ),
            category=Category3Enum.INTERNAL,
            status=Status51Enum.CANCELLED,
            account_holder=ResourceReference5(
                description='description0',
                id='id0',
                reference='reference4'
            ),
            balance_account=ResourceReference1(
                description='description2',
                id='id2',
                reference='reference2'
            ),
            balance_platform='balancePlatform2',
            balances=[
                BalanceMutation(
                    balance=224,
                    currency='currency0',
                    received=214,
                    reserved=158
                ),
                BalanceMutation(
                    balance=224,
                    currency='currency0',
                    received=214,
                    reserved=158
                ),
                BalanceMutation(
                    balance=224,
                    currency='currency0',
                    received=214,
                    reserved=158
                )
            ],
            category_data=BankCategoryData(
                priority=Priority1Enum.INSTANT,
                mtype=Type310Enum.BANK
            )
        )
    ]
)
```

