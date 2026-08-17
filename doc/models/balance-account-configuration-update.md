
# Balance Account Configuration Update

## Structure

`BalanceAccountConfigurationUpdate`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `description` | `str` | Optional | The description used for all payouts initiated by this payout schedule.<br><br>Maximum length: 140 characters. If your description is longer, it may be truncated.<br><br>Default value: The `defaultDescription` from the balance platform schedule that you are applying. |
| `enabled` | `bool` | Optional | Specifies whether the payout schedule is enabled immediately after it is created. |
| `frequency` | [`Frequency1Enum`](../../doc/models/frequency-1-enum.md) | Optional | The frequency of payouts initiated by this payout schedule.<br><br>Possible values:<br><br>* daily<br>* weekdays<br>* weekly<br>* monthly<br><br>Default value: The `defaultFrequency` from the balance platform schedule that you are applying. |
| `frequency_value` | `int` | Optional | The date of the month or day of the week when payouts are initiated. Allowed only if `frequency` is **monthly** or **weekly**.<br><br>Possible values if `frequency` is **monthly**: **[1 - 31]**.<br><br>* If your specified date happens on a weekend, the payout is initiated on the next business day.<br>* If your specified date (**29**, **30**, or **31**) does not exist in a month, the payout is initiated on the last day of that month.<br><br>Possible values if `frequency` is **weekly**: **[1 - 5]**.<br><br>Default value: The `defaultFrequencyValue` from the balance platform schedule that you are applying. |
| `max_payout_amount` | `int` | Optional | The maximum amount that can be paid out from balance accounts that use this payout schedule.<br><br>Default value: **0** |
| `min_payout_amount` | `int` | Optional | The minimum amount that can be paid out from balance accounts that use this payout schedule.<br><br>Default value: **0** |
| `reference` | `str` | Optional | The merchant reference that will be shown only in the schedule. |
| `reference_for_beneficiary` | `str` | Optional | The reference for beneficiary used for all payouts initiated by this payout schedule. This reference is sent to the recipient of the transfer and is included in all webhooks related to the payout.<br><br>Supported characters: **a-z**, **A-Z**, **0-9**, **-** and space. Spaces might be replaced with **-** if the recipient bank or payment infrastructure does not allow spaces.<br><br>Default value: The `defaultReferenceForBeneficiary` from the balance platform schedule that you are applying. |
| `retained_amount` | `int` | Optional | The amount of funds that must remain available in the balance account after an execution of the payout schedule. If the funds in the balance account are less than the retained amount, the execution is not initiated.<br><br>Default value: **0** |
| `sales_day_closing_time` | `str` | Optional | The time of day when the sales day is closed in balance account time zone. The sales day closing time can be between 00:00 to 07:00.<br><br>Format: **HH:mm:ss** |
| `transfer_instrument_id` | `str` | Optional | The unique identifier of the transfer instrument to which the funds are paid out. |

## Example

```python
from adyen.models.balance_account_configuration_update import BalanceAccountConfigurationUpdate
from adyen.models.frequency_1_enum import Frequency1Enum

balance_account_configuration_update = BalanceAccountConfigurationUpdate(
    description='description0',
    enabled=False,
    frequency=Frequency1Enum.WEEKDAYS,
    frequency_value=70,
    max_payout_amount=42
)
```

