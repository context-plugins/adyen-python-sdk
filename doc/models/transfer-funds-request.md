
# Transfer Funds Request

## Structure

`TransferFundsRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amount` | [`Amount`](../../doc/models/amount.md) | Required | The amount to be transferred. |
| `destination_account_code` | `str` | Required | The code of the account to which the funds are to be credited.<br><br>> The state of the Account Holder of this account must be Active. |
| `merchant_reference` | `str` | Optional | A value that can be supplied at the discretion of the executing user in order to link multiple transactions to one another. |
| `source_account_code` | `str` | Required | The code of the account from which the funds are to be debited.<br><br>> The state of the Account Holder of this account must be Active and allow payouts. |
| `transfer_code` | `str` | Required | The code related to the type of transfer being performed.<br><br>> The permitted codes differ for each platform account and are defined in their service level agreement. |

## Example

```python
from adyen.models.amount import Amount
from adyen.models.transfer_funds_request import TransferFundsRequest

transfer_funds_request = TransferFundsRequest(
    amount=Amount(
        currency='currency2',
        value=110
    ),
    destination_account_code='destinationAccountCode2',
    source_account_code='sourceAccountCode8',
    transfer_code='transferCode0',
    merchant_reference='merchantReference2'
)
```

