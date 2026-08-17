
# Transaction Search Response

## Structure

`TransactionSearchResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `links` | [`Links21`](../../doc/models/links-21.md) | Optional | Contains links to the next and previous page whenever applicable. |
| `data` | [`List[Transaction]`](../../doc/models/transaction.md) | Optional | Contains the transactions that match the query parameters. |

## Example

```python
import dateutil.parser

from adyen.models.amount_17 import Amount17
from adyen.models.bank_category_data import BankCategoryData
from adyen.models.links_21 import Links21
from adyen.models.links_element import LinksElement
from adyen.models.payment_instrument_21 import PaymentInstrument21
from adyen.models.priority_1_enum import Priority1Enum
from adyen.models.resource_reference_3 import ResourceReference3
from adyen.models.resource_reference_4 import ResourceReference4
from adyen.models.status_72_enum import Status72Enum
from adyen.models.transaction import Transaction
from adyen.models.transaction_search_response import TransactionSearchResponse
from adyen.models.transfer_view_2 import TransferView2
from adyen.models.type_310_enum import Type310Enum

transaction_search_response = TransactionSearchResponse(
    links=Links21(
        next=LinksElement(
            href='href4'
        ),
        prev=LinksElement(
            href='href8'
        )
    ),
    data=[
        Transaction(
            account_holder=ResourceReference3(
                description='description0',
                id='id0',
                reference='reference4'
            ),
            amount=Amount17(
                currency='currency2',
                value=110
            ),
            balance_account=ResourceReference4(
                description='description2',
                id='id2',
                reference='reference2'
            ),
            balance_platform='balancePlatform2',
            booking_date=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
            id='id0',
            status=Status72Enum.BOOKED,
            value_date=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
            creation_date=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
            description='description0',
            payment_instrument=PaymentInstrument21(
                description='description0',
                id='id0',
                reference='reference6',
                token_type='tokenType6'
            ),
            reference_for_beneficiary='referenceForBeneficiary0',
            transfer=TransferView2(
                reference='reference4',
                category_data=BankCategoryData(
                    priority=Priority1Enum.INSTANT,
                    mtype=Type310Enum.BANK
                ),
                id='id8'
            )
        )
    ]
)
```

