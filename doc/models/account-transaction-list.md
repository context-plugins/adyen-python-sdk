
# Account Transaction List

## Structure

`AccountTransactionList`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_code` | `str` | Optional | The code of the account. |
| `has_next_page` | `bool` | Optional | Indicates whether there is a next page of transactions available. |
| `transactions` | [`List[Transaction1]`](../../doc/models/transaction-1.md) | Optional | The list of transactions. |

## Example

```python
import dateutil.parser

from adyen.models.account_transaction_list import AccountTransactionList
from adyen.models.amount import Amount
from adyen.models.bank_account_detail import BankAccountDetail
from adyen.models.transaction_1 import Transaction1

account_transaction_list = AccountTransactionList(
    account_code='accountCode0',
    has_next_page=False,
    transactions=[
        Transaction1(
            amount=Amount(
                currency='currency2',
                value=110
            ),
            bank_account_detail=BankAccountDetail(
                account_number='accountNumber8',
                account_type='accountType4',
                bank_account_name='bankAccountName4',
                bank_account_reference='bankAccountReference4',
                bank_account_uuid='bankAccountUUID0'
            ),
            capture_merchant_reference='captureMerchantReference8',
            capture_psp_reference='capturePspReference6',
            creation_date=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
        ),
        Transaction1(
            amount=Amount(
                currency='currency2',
                value=110
            ),
            bank_account_detail=BankAccountDetail(
                account_number='accountNumber8',
                account_type='accountType4',
                bank_account_name='bankAccountName4',
                bank_account_reference='bankAccountReference4',
                bank_account_uuid='bankAccountUUID0'
            ),
            capture_merchant_reference='captureMerchantReference8',
            capture_psp_reference='capturePspReference6',
            creation_date=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
        ),
        Transaction1(
            amount=Amount(
                currency='currency2',
                value=110
            ),
            bank_account_detail=BankAccountDetail(
                account_number='accountNumber8',
                account_type='accountType4',
                bank_account_name='bankAccountName4',
                bank_account_reference='bankAccountReference4',
                bank_account_uuid='bankAccountUUID0'
            ),
            capture_merchant_reference='captureMerchantReference8',
            capture_psp_reference='capturePspReference6',
            creation_date=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
        )
    ]
)
```

