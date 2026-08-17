
# Transaction 1

## Structure

`Transaction1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amount` | [`Amount`](../../doc/models/amount.md) | Optional | The amount of the transaction. |
| `bank_account_detail` | [`BankAccountDetail`](../../doc/models/bank-account-detail.md) | Optional | The details of the bank account to where a payout was made. |
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
| `transaction_status` | [`TransactionStatus1Enum`](../../doc/models/transaction-status-1-enum.md) | Optional | The status of the transaction.<br><br>> Permitted values: `PendingCredit`, `CreditFailed`, `CreditClosed`, `CreditSuspended`, `Credited`, `Converted`, `PendingDebit`, `DebitFailed`, `Debited`, `DebitReversedReceived`, `DebitedReversed`, `ChargebackReceived`, `Chargeback`, `ChargebackReversedReceived`, `ChargebackReversed`, `Payout`, `PayoutReversed`, `FundTransfer`, `PendingFundTransfer`, `ManualCorrected`. |
| `transfer_code` | `str` | Optional | The transfer code of the transaction. |

## Example

```python
import dateutil.parser

from adyen.models.amount import Amount
from adyen.models.bank_account_detail import BankAccountDetail
from adyen.models.transaction_1 import Transaction1

transaction_1 = Transaction1(
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
    capture_merchant_reference='captureMerchantReference4',
    capture_psp_reference='capturePspReference4',
    creation_date=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
)
```

