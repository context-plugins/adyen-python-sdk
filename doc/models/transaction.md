
# Transaction

*This model accepts additional fields of type Any.*

## Structure

`Transaction`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amount` | [`Amount16`](../../doc/models/amount-16.md) | Optional | - |
| `bank_account_detail` | [`BankAccountDetail1`](../../doc/models/bank-account-detail-1.md) | Optional | - |
| `capture_merchant_reference` | `str` | Optional | The merchant reference of a related capture. |
| `capture_psp_reference` | `str` | Optional | The psp reference of a related capture. |
| `creation_date` | `datetime` | Optional | The date on which the transaction was performed. |
| `description` | `str` | Optional | A description of the transaction. |
| `destination_account_code` | `str` | Optional | The code of the account to which funds were credited during an outgoing fund transfer. |
| `dispute_psp_reference` | `str` | Optional | The psp reference of the related dispute. |
| `dispute_reason_code` | `str` | Optional | The reason code of a dispute. |
| `merchant_reference` | `str` | Optional | The merchant reference of a transaction. |
| `payment_psp_reference` | `str` | Optional | The psp reference of the related authorisation or transfer. |
| `payout_psp_reference` | `str` | Optional | The psp reference of the related payout. |
| `psp_reference` | `str` | Optional | The psp reference of a transaction. |
| `source_account_code` | `str` | Optional | The code of the account from which funds were debited during an incoming fund transfer. |
| `transaction_status` | [`TransactionStatus1`](../../doc/models/transaction-status-1.md) | Optional | - |
| `transfer_code` | `str` | Optional | The transfer code of the transaction. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from adyen.models.amount_16 import Amount16
from adyen.models.bank_account_detail_1 import BankAccountDetail1
from adyen.models.transaction import Transaction

transaction = Transaction(
    amount=Amount16(
        currency='currency2',
        value=110,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    bank_account_detail=BankAccountDetail1(
        account_number='accountNumber8',
        account_type='accountType4',
        bank_account_name='bankAccountName4',
        bank_account_reference='bankAccountReference4',
        bank_account_uuid='bankAccountUUID0',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    capture_merchant_reference='captureMerchantReference2',
    capture_psp_reference='capturePspReference6',
    creation_date=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

