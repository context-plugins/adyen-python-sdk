
# Counterparty 10

*This model accepts additional fields of type Any.*

## Structure

`Counterparty10`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_holder_id` | `str` | Optional | The unique identifier of the account holder that receives the grant. |
| `balance_account_id` | `str` | Optional | The unique identifier of the balance account where the funds are disbursed. The balance account must belong to the specified account holder. |
| `transfer_instrument_id` | `str` | Optional | The unique identifier of the transfer instrument where the funds are disbursed. The transfer instrument must belong to the legal entity of the specified account holder. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.counterparty_10 import Counterparty10

counterparty_10 = Counterparty10(
    account_holder_id='accountHolderId6',
    balance_account_id='balanceAccountId4',
    transfer_instrument_id='transferInstrumentId8',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

