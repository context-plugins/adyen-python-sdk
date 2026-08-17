
# Update Sweep Configuration V2

## Structure

`UpdateSweepConfigurationV2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `category` | [`Category1Enum`](../../doc/models/category-1-enum.md) | Optional | The type of transfer that results from the sweep.<br><br>Possible values:<br><br>- **bank**: Sweep to a [transfer instrument](https://docs.adyen.com/api-explorer/#/legalentity/latest/post/transferInstruments__resParam_id).<br><br>- **internal**: Transfer to another [balance account](https://docs.adyen.com/api-explorer/#/balanceplatform/latest/post/balanceAccounts__resParam_id) within your platform.<br><br>Required when setting `priorities`. |
| `counterparty` | [`SweepCounterparty1`](../../doc/models/sweep-counterparty-1.md) | Optional | The destination or the source of the funds, depending on the sweep `type`.<br><br>Either a `balanceAccountId`, `transferInstrumentId`, or `merchantAccount` is required. |
| `currency` | `str` | Optional | The three-character [ISO currency code](https://docs.adyen.com/development-resources/currency-codes) in uppercase. For example, **EUR**.<br><br>The sweep currency must match any of the [balances currencies](https://docs.adyen.com/api-explorer/#/balanceplatform/latest/get/balanceAccounts/{id}__resParam_balances). |
| `description` | `str` | Optional | The message that will be used in the sweep transfer's description body with a maximum length of 140 characters.<br><br>If the message is longer after replacing placeholders, the message will be cut off at 140 characters. |
| `id` | `str` | Optional, Read-only | The unique identifier of the sweep. |
| `priorities` | [`List[Priority1Enum]`](../../doc/models/priority-1-enum.md) | Optional | The list of priorities for the bank transfer. This sets the speed at which the transfer is sent and the fees that you have to pay. You can provide multiple priorities, ordered by your preference. Adyen will try to pay out using the priorities in the given order. If the first priority is not currently supported or enabled for your platform, the system will try the next one, and so on.<br><br>The request will be accepted as long as **at least one** of the provided priorities is valid (i.e., supported by Adyen and activated for your platform). For example, if you provide `["wire","regular"]`, and `wire` is not supported but `regular` is, the request will still be accepted and processed.<br><br>Possible values:<br><br>* **regular**: For normal, low-value transactions.<br><br>* **fast**: A faster way to transfer funds, but the fees are higher. Recommended for high-priority, low-value transactions.<br><br>* **wire**: The fastest way to transfer funds, but this has the highest fees. Recommended for high-priority, high-value transactions.<br><br>* **instant**: For instant funds transfers within the United States and in [SEPA locations](https://www.ecb.europa.eu/paym/integration/retail/sepa/html/index.en.html).<br><br>* **crossBorder**: For high-value transfers to a recipient in a different country.<br><br>* **internal**: For transfers to an Adyen-issued business bank account (by bank account number/IBAN).<br><br>Set `category` to **bank**. For more details, see optional priorities setup for [marketplaces](https://docs.adyen.com/marketplaces/payout-to-users/scheduled-payouts#optional-priorities-setup) or [platforms](https://docs.adyen.com/platforms/payout-to-users/scheduled-payouts#optional-priorities-setup). |
| `reason` | [`ReasonEnum`](../../doc/models/reason-enum.md) | Optional, Read-only | The reason for disabling the sweep. |
| `reason_detail` | `str` | Optional, Read-only | The human readable reason for disabling the sweep. |
| `reference` | `str` | Optional | Your reference for the sweep configuration.<br><br>**Constraints**: *Maximum Length*: `80` |
| `reference_for_beneficiary` | `str` | Optional | The reference sent to or received from the counterparty. Only alphanumeric characters are allowed.<br><br>**Constraints**: *Maximum Length*: `80` |
| `schedule` | [`SweepSchedule1`](../../doc/models/sweep-schedule-1.md) | Optional | The schedule when the `triggerAmount` is evaluated. If the balance meets the threshold, funds are pushed out of or pulled in to the balance account. |
| `status` | [`Status6Enum`](../../doc/models/status-6-enum.md) | Optional | The status of the sweep. If not provided, by default, this is set to **active**.<br><br>Possible values:<br><br>* **active**:  the sweep is enabled and funds will be pulled in or pushed out based on the defined configuration.<br><br>* **inactive**: the sweep is disabled and cannot be triggered. |
| `sweep_amount` | [`Amount17`](../../doc/models/amount-17.md) | Optional | The amount that must be pushed out or pulled in. You can configure either `sweepAmount` or `targetAmount`, not both. |
| `target_amount` | [`Amount17`](../../doc/models/amount-17.md) | Optional | The amount that must be available in the balance account after the sweep. You can configure either `sweepAmount` or `targetAmount`, not both. |
| `trigger_amount` | [`Amount17`](../../doc/models/amount-17.md) | Optional | The threshold amount that triggers the sweep. If not provided, by default, the amount is set to zero. The `triggerAmount` is evaluated according to the specified `schedule.type`.<br><br>* For `type` **pull**, if the balance is less than or equal to the `triggerAmount`, funds are pulled in to the balance account.<br><br>* For `type` **push**, if the balance is more than or equal to the `triggerAmount`, funds are pushed out of the balance account. |
| `mtype` | [`Type72Enum`](../../doc/models/type-72-enum.md) | Optional | The direction of sweep, whether pushing out or pulling in funds to the balance account. If not provided, by default, this is set to **push**.<br><br>Possible values:<br><br>* **push**: _push out funds_ to a destination balance account or transfer instrument.<br><br>* **pull**: _pull in funds_ from a source merchant account, transfer instrument, or balance account.<br><br>**Default**: `"push"` |

## Example

```python
from adyen.models.category_1_enum import Category1Enum
from adyen.models.sweep_counterparty_1 import SweepCounterparty1
from adyen.models.type_72_enum import Type72Enum
from adyen.models.update_sweep_configuration_v_2 import UpdateSweepConfigurationV2

update_sweep_configuration_v_2 = UpdateSweepConfigurationV2(
    category=Category1Enum.BANK,
    counterparty=SweepCounterparty1(
        balance_account_id='balanceAccountId0',
        merchant_account='merchantAccount0',
        transfer_instrument_id='transferInstrumentId4'
    ),
    currency='currency2',
    description='description2',
    mtype=Type72Enum.PUSH
)
```

