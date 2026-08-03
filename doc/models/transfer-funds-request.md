
# Transfer Funds Request

*This model accepts additional fields of type Any.*

## Structure

`TransferFundsRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amount` | [`Amount16`](../../doc/models/amount-16.md) | Required | - |
| `destination_account_code` | `str` | Required | The code of the account to which the funds are to be credited.<br><br>> The state of the Account Holder of this account must be Active. |
| `merchant_reference` | `str` | Optional | A value that can be supplied at the discretion of the executing user in order to link multiple transactions to one another. |
| `source_account_code` | `str` | Required | The code of the account from which the funds are to be debited.<br><br>> The state of the Account Holder of this account must be Active and allow payouts. |
| `transfer_code` | `str` | Required | The code related to the type of transfer being performed.<br><br>> The permitted codes differ for each platform account and are defined in their service level agreement. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.amount_16 import Amount16
from adyen.models.transfer_funds_request import TransferFundsRequest

transfer_funds_request = TransferFundsRequest(
    amount=Amount16(
        currency='currency2',
        value=110,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    destination_account_code='destinationAccountCode2',
    source_account_code='sourceAccountCode8',
    transfer_code='transferCode0',
    merchant_reference='merchantReference2',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

