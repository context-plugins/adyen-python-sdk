
# Sweep Counterparty

*This model accepts additional fields of type Any.*

## Structure

`SweepCounterparty`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `balance_account_id` | `str` | Optional | The unique identifier of the destination or source [balance account](https://docs.adyen.com/api-explorer/#/balanceplatform/latest/post/balanceAccounts__resParam_id).<br><br>> If you are updating the counterparty from a transfer instrument to a balance account, set `transferInstrumentId` to **null**. |
| `merchant_account` | `str` | Optional | The merchant account that will be the source of funds.<br><br>You can only use this parameter with sweeps of `type` **pull** and if you are processing payments with Adyen. |
| `transfer_instrument_id` | `str` | Optional | The unique identifier of the destination or source [transfer instrument](https://docs.adyen.com/api-explorer/legalentity/latest/post/transferInstruments#responses-200-id) depending on the sweep `type`<br><br>. To set up automated top-up sweeps to balance accounts in your [marketplace](https://docs.adyen.com/marketplaces/top-up-balance-account/#before-you-begin) or [platform](https://docs.adyen.com/platforms/top-up-balance-account/#before-you-begin), use this parameter in combination with a `merchantAccount` and a sweep `type` of **pull**.<br><br>Top-up sweeps start a direct debit request from the source transfer instrument. Contact Adyen Support to enable this feature.> If you are updating the counterparty from a balance account to a transfer instrument, set `balanceAccountId` to **null**. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.sweep_counterparty import SweepCounterparty

sweep_counterparty = SweepCounterparty(
    balance_account_id='balanceAccountId4',
    merchant_account='merchantAccount6',
    transfer_instrument_id='transferInstrumentId2',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

