
# Balance Platform Configurations

## Structure

`BalancePlatformConfigurations`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `balance_platform_payout_schedules` | [`List[BalancePlatformConfiguration]`](../../doc/models/balance-platform-configuration.md) | Required | Contains a list of the payout schedules configured in your balance platform. |

## Example

```python
import dateutil.parser

from adyen.models.balance_platform_configuration import BalancePlatformConfiguration
from adyen.models.balance_platform_configurations import BalancePlatformConfigurations
from adyen.models.local_time_2 import LocalTime2

balance_platform_configurations = BalancePlatformConfigurations(
    balance_platform_payout_schedules=[
        BalancePlatformConfiguration(
            balance_platform_id='balancePlatformId0',
            created_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
            payout_schedule_description='payoutScheduleDescription6',
            user_settlement_delay=126,
            user_settlement_time=LocalTime2(
                hour=136,
                minute=138,
                nano=162,
                second=200
            ),
            user_settlement_time_zone='userSettlementTimeZone4',
            automatic_application=False,
            country_code='countryCode2',
            currency='currency2',
            default_description='defaultDescription6',
            default_frequency='defaultFrequency6'
        )
    ]
)
```

