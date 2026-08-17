
# Balance Account Configurations

## Structure

`BalanceAccountConfigurations`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `balance_account_payout_schedules` | [`List[BalanceAccountConfiguration]`](../../doc/models/balance-account-configuration.md) | Required | Contains a list of the Balance Account payout schedules. |
| `link` | [`Link2`](../../doc/models/link-2.md) | Required | Contains links to the next and previous page whenever applicable. |

## Example

```python
import dateutil.parser

from adyen.models.balance_account_configuration import BalanceAccountConfiguration
from adyen.models.balance_account_configurations import BalanceAccountConfigurations
from adyen.models.link_2 import Link2
from adyen.models.links_element import LinksElement

balance_account_configurations = BalanceAccountConfigurations(
    balance_account_payout_schedules=[
        BalanceAccountConfiguration(
            balance_account_id='balanceAccountId0',
            balance_platform_payout_schedule_id='balancePlatformPayoutScheduleId8',
            created_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
            transfer_instrument_id='transferInstrumentId4',
            currency='currency8',
            description='description2',
            enabled=False,
            frequency='frequency6',
            frequency_value=138
        )
    ],
    link=Link2(
        first=LinksElement(
            href='href2'
        ),
        last=LinksElement(
            href='href2'
        ),
        next=LinksElement(
            href='href4'
        ),
        previous=LinksElement(
            href='href0'
        ),
        mself=LinksElement(
            href='href0'
        )
    )
)
```

