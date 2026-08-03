
# Balance Account Configuration

*This model accepts additional fields of type Any.*

## Structure

`BalanceAccountConfiguration`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `balance_account_id` | `str` | Required | The unique identifier of the balance account to which you apply the payout schedule. |
| `balance_platform_payout_schedule_id` | `str` | Required | The unique identifier of the balance platform payout schedule that is applied to the balance account. |
| `created_at` | `datetime` | Required | The date and time when the payout schedule was created. |
| `currency` | `str` | Optional | The three-character [ISO code](https://docs.adyen.com/development-resources/currency-codes) of the currency used for this schedule. |
| `description` | `str` | Optional | The description used for all payouts initiated by this payout schedule.<br><br>Maximum length: 140 characters. If your description is longer, it may be truncated.<br><br>Default value: The `defaultDescription` from the balance platform schedule that you are applying. |
| `enabled` | `bool` | Optional | Specifies whether the payout schedule is active. |
| `frequency` | `str` | Optional | The frequency of payouts initiated by this payout schedule.<br><br>Possible values:<br><br>* daily<br>* weekdays<br>* weekly<br>* monthly<br><br>Default value: The `defaultFrequency` from the balance platform schedule that you are applying. |
| `frequency_value` | `int` | Optional | The date of the month or day of the week when payouts are initiated. Allowed only if `frequency` is **monthly** or **weekly**.<br><br>Possible values if `frequency` is **monthly**: **[1 - 31]**.<br><br>* If your specified date happens on a weekend, the payout is initiated on the next business day.<br>* If your specified date (**29**, **30**, or **31**) does not exist in a month, the payout is initiated  on the last day of that month.<br><br>Possible values if `frequency` is **weekly**: **[1 - 5]**.<br><br>Default value: The `defaultFrequencyValue` from the balance platform schedule that you are applying. |
| `id` | `str` | Optional | The unique identifier of the payout schedule for the balance account. |
| `max_payout_amount` | `int` | Optional | The maximum amount that can be paid out from balance accounts that use this payout schedule.<br><br>Default value: **0** |
| `min_payout_amount` | `int` | Optional | The minimum amount that can be paid out from balance accounts that use this payout schedule.<br><br>Default value: **0** |
| `reference` | `str` | Optional | Your reference for the payout schedule. This reference does not appear on statements of payouts initiated by the payout schedule. |
| `reference_for_beneficiary` | `str` | Optional | The reference for beneficiary used for all payouts initiated by this payout schedule. This reference is sent to the recipient of the payout and is included in all webhooks related to the payout.<br><br>Supported characters: **a-z**, **A-Z**, **0-9**.<br><br>Default value: The `defaultReferenceForBeneficiary` from the balance platform schedule that you are applying. |
| `retained_amount` | `int` | Optional | The amount of funds that must remain available in the balance account after an execution of the payout schedule. If the funds in the balance account are less than the retained amount, the execution is not initiated.<br><br>Default value: **0** |
| `sales_day_closing_time` | `str` | Optional | The time of day when the sales day is closed in balance account time zone. The sales day closing time can be between 00:00 to 07:00.<br><br>Format: **HH:mm:ss** |
| `transfer_instrument_id` | `str` | Required | The unique identifier of the transfer instrument to which the funds are paid out. |
| `updated_at` | `datetime` | Optional | The date and time when the payout schedule was updated. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from adyen.models.balance_account_configuration import BalanceAccountConfiguration

balance_account_configuration = BalanceAccountConfiguration(
    balance_account_id='balanceAccountId4',
    balance_platform_payout_schedule_id='balancePlatformPayoutScheduleId2',
    created_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    transfer_instrument_id='transferInstrumentId0',
    currency='currency2',
    description='description2',
    enabled=False,
    frequency='frequency8',
    frequency_value=216,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

