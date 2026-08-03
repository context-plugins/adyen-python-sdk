
# Transaction Search Response

*This model accepts additional fields of type Any.*

## Structure

`TransactionSearchResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `links` | [`Links3`](../../doc/models/links-3.md) | Optional | - |
| `data` | [`List[Transaction1]`](../../doc/models/transaction-1.md) | Optional | Contains the transactions that match the query parameters. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from adyen.models.amount_5 import Amount5
from adyen.models.bank_category_data import BankCategoryData
from adyen.models.links_3 import Links3
from adyen.models.next import Next
from adyen.models.payment_instrument_2 import PaymentInstrument2
from adyen.models.prev import Prev
from adyen.models.priority import Priority
from adyen.models.resource_reference import ResourceReference
from adyen.models.status_71 import Status71
from adyen.models.transaction_1 import Transaction1
from adyen.models.transaction_search_response import TransactionSearchResponse
from adyen.models.transfer_view import TransferView
from adyen.models.type_312 import Type312

transaction_search_response = TransactionSearchResponse(
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
        Transaction1(
            account_holder=ResourceReference(
                description='description0',
                id='id0',
                reference='reference4',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            amount=Amount5(
                currency='currency2',
                value=110,
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
            booking_date=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
            id='id0',
            status=Status71.BOOKED,
            value_date=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
            creation_date=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
            description='description0',
            payment_instrument=PaymentInstrument2(
                description='description0',
                id='id0',
                reference='reference6',
                token_type='tokenType6',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            reference_for_beneficiary='referenceForBeneficiary0',
            transfer=TransferView(
                reference='reference4',
                category_data=BankCategoryData(
                    priority=Priority.INSTANT,
                    mtype=Type312.BANK,
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                ),
                id='id8',
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

