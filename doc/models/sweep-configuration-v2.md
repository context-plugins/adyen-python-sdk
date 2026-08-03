
# Sweep Configuration V2

*This model accepts additional fields of type Any.*

## Structure

`SweepConfigurationV2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `category` | [`Category`](../../doc/models/category.md) | Optional | - |
| `counterparty` | [`SweepCounterparty`](../../doc/models/sweep-counterparty.md) | Required | - |
| `currency` | `str` | Required | The three-character [ISO currency code](https://docs.adyen.com/development-resources/currency-codes) in uppercase. For example, **EUR**.<br><br>The sweep currency must match any of the [balances currencies](https://docs.adyen.com/api-explorer/#/balanceplatform/latest/get/balanceAccounts/{id}__resParam_balances). |
| `description` | `str` | Optional | The message that will be used in the sweep transfer's description body with a maximum length of 140 characters.<br><br>If the message is longer after replacing placeholders, the message will be cut off at 140 characters. |
| `id` | `str` | Required, Read-only | The unique identifier of the sweep. |
| `priorities` | [`List[Priority]`](../../doc/models/priority.md) | Optional | The list of priorities for the bank transfer. This sets the speed at which the transfer is sent and the fees that you have to pay. You can provide multiple priorities, ordered by your preference. Adyen will try to pay out using the priorities in the given order. If the first priority is not currently supported or enabled for your platform, the system will try the next one, and so on.<br><br>The request will be accepted as long as **at least one** of the provided priorities is valid (i.e., supported by Adyen and activated for your platform). For example, if you provide `["wire","regular"]`, and `wire` is not supported but `regular` is, the request will still be accepted and processed.<br><br>Possible values:<br><br>* **regular**: For normal, low-value transactions.<br><br>* **fast**: A faster way to transfer funds, but the fees are higher. Recommended for high-priority, low-value transactions.<br><br>* **wire**: The fastest way to transfer funds, but this has the highest fees. Recommended for high-priority, high-value transactions.<br><br>* **instant**: For instant funds transfers within the United States and in [SEPA locations](https://www.ecb.europa.eu/paym/integration/retail/sepa/html/index.en.html).<br><br>* **crossBorder**: For high-value transfers to a recipient in a different country.<br><br>* **internal**: For transfers to an Adyen-issued business bank account (by bank account number/IBAN).<br><br>Set `category` to **bank**. For more details, see optional priorities setup for [marketplaces](https://docs.adyen.com/marketplaces/payout-to-users/scheduled-payouts#optional-priorities-setup) or [platforms](https://docs.adyen.com/platforms/payout-to-users/scheduled-payouts#optional-priorities-setup). |
| `reason` | [`Reason`](../../doc/models/reason.md) | Optional, Read-only | - |
| `reason_detail` | `str` | Optional, Read-only | The human readable reason for disabling the sweep. |
| `reference` | `str` | Optional | Your reference for the sweep configuration.<br><br>**Constraints**: *Maximum Length*: `80` |
| `reference_for_beneficiary` | `str` | Optional | The reference sent to or received from the counterparty. Only alphanumeric characters are allowed.<br><br>**Constraints**: *Maximum Length*: `80` |
| `schedule` | [`SweepSchedule`](../../doc/models/sweep-schedule.md) | Required | - |
| `status` | [`Status51`](../../doc/models/status-51.md) | Optional | - |
| `sweep_amount` | [`SweepAmount`](../../doc/models/sweep-amount.md) | Optional | - |
| `target_amount` | [`TargetAmount`](../../doc/models/target-amount.md) | Optional | - |
| `trigger_amount` | [`TriggerAmount`](../../doc/models/trigger-amount.md) | Optional | - |
| `mtype` | [`Type7`](../../doc/models/type-7.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.category import Category
from adyen.models.priority import Priority
from adyen.models.reason import Reason
from adyen.models.sweep_configuration_v_2 import SweepConfigurationV2
from adyen.models.sweep_counterparty import SweepCounterparty
from adyen.models.sweep_schedule import SweepSchedule
from adyen.models.type_6 import Type6

sweep_configuration_v_2 = SweepConfigurationV2(
    counterparty=SweepCounterparty(
        balance_account_id='balanceAccountId0',
        merchant_account='merchantAccount0',
        transfer_instrument_id='transferInstrumentId4',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    currency='currency6',
    id='id6',
    schedule=SweepSchedule(
        mtype=Type6.WEEKLY,
        cron_expression='cronExpression4',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    category=Category.BANK,
    description='description6',
    priorities=[
        Priority.INSTANT
    ],
    reason=Reason.ACCOUNTHIERARCHYNOTACTIVE,
    reason_detail='reasonDetail2',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

