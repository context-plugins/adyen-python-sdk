
# Balance Platform Configuration

## Structure

`BalancePlatformConfiguration`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `automatic_application` | `bool` | Optional | Specifies whether this payout schedule is automatically applied to new balance accounts. |
| `balance_platform_id` | `str` | Required | The balance platform to which the payout schedule applies. |
| `country_code` | `str` | Optional | The two-letter [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) code of the country to which the payout schedule applies. |
| `created_at` | `datetime` | Required | The date when the payout schedule was created. |
| `currency` | `str` | Optional | The three-character [ISO code](https://docs.adyen.com/development-resources/currency-codes) of the currency used for the payout schedule. |
| `default_description` | `str` | Optional | The default description for payouts initiated by this payout schedule. |
| `default_frequency` | `str` | Optional | The default frequency of payouts initiated by this payout schedule. |
| `default_frequency_value` | `int` | Optional | The default value for date of the month or day of the week when payouts are initiated. Allowed only if `defaultFrequency` is **monthly** or **weekly**.<br><br>Possible values if `defaultFrequency` is **monthly**: **[1 - 31]**.<br><br>* If your specified date happens on a weekend, the payout is initiated on the next business day.<br>* If your specified date (**29**, **30**, or **31**) does not exist in a month, the payout is initiated  on the last day of that month.<br><br>Possible values if `defaultFrequency` is **weekly**: **[1 - 5]**. |
| `default_reference` | `str` | Optional | Your internal default reference for the payout schedule.When the payout schedule is applied to a balance account, this reference is also used for that payout schedule. |
| `default_reference_for_beneficiary` | `str` | Optional | The default reference for beneficiary for payouts initiated by this payout schedule. |
| `enabled` | `bool` | Optional | Specifies whether the payout schedule is enabled immediately after it is created. |
| `id` | `str` | Optional | The unique identifier of the payout schedule for your balance platform. |
| `max_payout_amount` | `int` | Optional | The maximum amount that can be paid out from balance accounts that use this payout schedule.<br><br>Default value: **0**, which means that there is no maximum limit. |
| `min_payout_amount` | `int` | Optional | The minimum amount that can be paid out from balance accounts that use this payout schedule.<br><br>Default value: **0**. |
| `payout_schedule_description` | `str` | Required | The type of payout schedule. This type indicates how fast funds are paid out to your user.<br><br>Possible values:<br><br>- **Standard**: The funds arrive in your user's transfer instrument two days after the funds are settled.<br>- **Accelerated**: The funds arrive to your user's transfer instrument the day after the funds are settled. |
| `retained_amount` | `int` | Optional | The amount of funds that must remain available in a balance account after an execution of the payout schedule. If the funds in the balance account are less than the retained amount, the execution is not initiated.<br><br>Default value: **0** |
| `updated_at` | `datetime` | Optional | The date when the payout schedule was updated. |
| `user_settlement_delay` | `int` | Required | The default [settlement delay](https://docs.adyen.com/platforms/settle-funds/#settlement-delay) for this payout schedule. |
| `user_settlement_time` | [`LocalTime2`](../../doc/models/local-time-2.md) | Required | The time when the payout funds are settled in your user's transfer instrument. |
| `user_settlement_time_zone` | `str` | Required | The timezone of the `userSettlementTime`. |

## Example

```python
import dateutil.parser

from adyen.models.balance_platform_configuration import BalancePlatformConfiguration
from adyen.models.local_time_2 import LocalTime2

balance_platform_configuration = BalancePlatformConfiguration(
    balance_platform_id='balancePlatformId2',
    created_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    payout_schedule_description='payoutScheduleDescription4',
    user_settlement_delay=102,
    user_settlement_time=LocalTime2(
        hour=136,
        minute=138,
        nano=162,
        second=200
    ),
    user_settlement_time_zone='userSettlementTimeZone6',
    automatic_application=False,
    country_code='countryCode0',
    currency='currency4',
    default_description='defaultDescription8',
    default_frequency='defaultFrequency8'
)
```

