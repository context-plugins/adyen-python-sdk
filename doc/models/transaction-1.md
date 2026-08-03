
# Transaction 1

*This model accepts additional fields of type Any.*

## Structure

`Transaction1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_holder` | [`ResourceReference`](../../doc/models/resource-reference.md) | Required | - |
| `amount` | [`Amount5`](../../doc/models/amount-5.md) | Required | - |
| `balance_account` | [`ResourceReference`](../../doc/models/resource-reference.md) | Required | - |
| `balance_platform` | `str` | Required | The unique identifier of the balance platform. |
| `booking_date` | `datetime` | Required | The date the transaction was booked into the balance account. |
| `creation_date` | `datetime` | Optional | The date and time when the event was triggered, in ISO 8601 extended format. For example, **2025-03-19T10:15:30+01:00**. |
| `description` | `str` | Optional | The `description` from the `/transfers` request. |
| `id` | `str` | Required | The unique identifier of the transaction. |
| `payment_instrument` | [`PaymentInstrument2`](../../doc/models/payment-instrument-2.md) | Optional | - |
| `reference_for_beneficiary` | `str` | Optional | The reference sent to or received from the counterparty.<br><br>* For outgoing funds, this is the [`referenceForBeneficiary`](https://docs.adyen.com/api-explorer/#/transfers/latest/post/transfers__resParam_referenceForBeneficiary) from the  [`/transfers`](https://docs.adyen.com/api-explorer/#/transfers/latest/post/transfers__reqParam_referenceForBeneficiary) request.<br><br>* For incoming funds, this is the reference from the sender. |
| `status` | [`Status71`](../../doc/models/status-71.md) | Required | - |
| `transfer` | [`TransferView`](../../doc/models/transfer-view.md) | Optional | - |
| `value_date` | `datetime` | Required | The date the transfer amount becomes available in the balance account. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from adyen.models.amount_5 import Amount5
from adyen.models.bank_category_data import BankCategoryData
from adyen.models.payment_instrument_2 import PaymentInstrument2
from adyen.models.priority import Priority
from adyen.models.resource_reference import ResourceReference
from adyen.models.status_71 import Status71
from adyen.models.transaction_1 import Transaction1
from adyen.models.transfer_view import TransferView
from adyen.models.type_312 import Type312

transaction_1 = Transaction1(
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
    balance_platform='balancePlatform8',
    booking_date=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    id='id6',
    status=Status71.BOOKED,
    value_date=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    creation_date=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    description='description6',
    payment_instrument=PaymentInstrument2(
        description='description0',
        id='id0',
        reference='reference6',
        token_type='tokenType6',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    reference_for_beneficiary='referenceForBeneficiary4',
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
```

