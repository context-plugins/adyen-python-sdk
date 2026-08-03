
# Grant Info Counterparty

An object containing the details of the receiving party of the grant.

*This model accepts additional fields of type Any.*

## Structure

`GrantInfoCounterparty`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `balance_account_id` | `str` | Optional | The unique identifier of the balance account where the funds are disbursed. The balance account must belong to the specified account holder. |
| `transfer_instrument_id` | `str` | Optional | The unique identifier of the transfer instrument where the funds are disbursed. The transfer instrument must belong to the legal entity of the specified account holder. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.grant_info_counterparty import GrantInfoCounterparty

grant_info_counterparty = GrantInfoCounterparty(
    balance_account_id='balanceAccountId2',
    transfer_instrument_id='transferInstrumentId6',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

