
# Balance Transfer Request

*This model accepts additional fields of type Any.*

## Structure

`BalanceTransferRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amount` | [`Amount5`](../../doc/models/amount-5.md) | Required | - |
| `from_merchant` | `str` | Required | The unique identifier of the source merchant account from which funds are deducted.<br><br>**Constraints**: *Minimum Length*: `1` |
| `reference` | `str` | Optional | A reference for the balance transfer. Maximum length: 80 characters.<br><br>**Constraints**: *Minimum Length*: `0`, *Maximum Length*: `80` |
| `to_merchant` | `str` | Required | The unique identifier of the destination merchant account to which funds are transferred.<br><br>**Constraints**: *Minimum Length*: `1` |
| `mtype` | [`BalanceTransferType2`](../../doc/models/balance-transfer-type-2.md) | Required | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.amount_5 import Amount5
from adyen.models.balance_transfer_request import BalanceTransferRequest
from adyen.models.balance_transfer_type_2 import BalanceTransferType2

balance_transfer_request = BalanceTransferRequest(
    amount=Amount5(
        currency='currency2',
        value=110,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    from_merchant='fromMerchant4',
    to_merchant='toMerchant4',
    mtype=BalanceTransferType2.DEBIT,
    reference='reference8',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

