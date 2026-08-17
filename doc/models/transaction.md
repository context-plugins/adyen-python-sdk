
# Transaction

## Structure

`Transaction`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_holder` | [`ResourceReference3`](../../doc/models/resource-reference-3.md) | Required | Contains information about the account holder associated with the `balanceAccount`. |
| `amount` | [`Amount17`](../../doc/models/amount-17.md) | Required | Contains information about the amount of the transaction. |
| `balance_account` | [`ResourceReference4`](../../doc/models/resource-reference-4.md) | Required | Contains information about the balance account involved in the transaction. |
| `balance_platform` | `str` | Required | The unique identifier of the balance platform. |
| `booking_date` | `datetime` | Required | The date the transaction was booked into the balance account. |
| `creation_date` | `datetime` | Optional | The date and time when the event was triggered, in ISO 8601 extended format. For example, **2025-03-19T10:15:30+01:00**. |
| `description` | `str` | Optional | The `description` from the `/transfers` request. |
| `id` | `str` | Required | The unique identifier of the transaction. |
| `payment_instrument` | [`PaymentInstrument21`](../../doc/models/payment-instrument-21.md) | Optional | Contains information about the payment instrument that was used for the transaction. |
| `reference_for_beneficiary` | `str` | Optional | The reference sent to or received from the counterparty.<br><br>* For outgoing funds, this is the [`referenceForBeneficiary`](https://docs.adyen.com/api-explorer/#/transfers/latest/post/transfers__resParam_referenceForBeneficiary) from the  [`/transfers`](https://docs.adyen.com/api-explorer/#/transfers/latest/post/transfers__reqParam_referenceForBeneficiary) request.<br><br>* For incoming funds, this is the reference from the sender. |
| `status` | [`Status72Enum`](../../doc/models/status-72-enum.md) | Required | The status of the transaction.<br><br>Possible values:<br><br>* **pending**: The transaction is still pending.<br><br>* **booked**: The transaction has been booked to the balance account. |
| `transfer` | [`TransferView2`](../../doc/models/transfer-view-2.md) | Optional | Contains information about the transfer related to the transaction. |
| `value_date` | `datetime` | Required | The date the transfer amount becomes available in the balance account. |

## Example

```python
import dateutil.parser

from adyen.models.amount_17 import Amount17
from adyen.models.bank_category_data import BankCategoryData
from adyen.models.payment_instrument_21 import PaymentInstrument21
from adyen.models.priority_1_enum import Priority1Enum
from adyen.models.resource_reference_3 import ResourceReference3
from adyen.models.resource_reference_4 import ResourceReference4
from adyen.models.status_72_enum import Status72Enum
from adyen.models.transaction import Transaction
from adyen.models.transfer_view_2 import TransferView2
from adyen.models.type_310_enum import Type310Enum

transaction = Transaction(
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
    balance_platform='balancePlatform0',
    booking_date=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    id='id8',
    status=Status72Enum.BOOKED,
    value_date=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    creation_date=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    description='description8',
    payment_instrument=PaymentInstrument21(
        description='description0',
        id='id0',
        reference='reference6',
        token_type='tokenType6'
    ),
    reference_for_beneficiary='referenceForBeneficiary2',
    transfer=TransferView2(
        reference='reference4',
        category_data=BankCategoryData(
            priority=Priority1Enum.INSTANT,
            mtype=Type310Enum.BANK
        ),
        id='id8'
    )
)
```

