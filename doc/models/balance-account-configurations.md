
# Balance Account Configurations

*This model accepts additional fields of type Any.*

## Structure

`BalanceAccountConfigurations`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `balance_account_payout_schedules` | [`List[BalanceAccountConfiguration]`](../../doc/models/balance-account-configuration.md) | Required | Contains a list of the Balance Account payout schedules. |
| `link` | [`Link`](../../doc/models/link.md) | Required | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from adyen.models.balance_account_configuration import BalanceAccountConfiguration
from adyen.models.balance_account_configurations import BalanceAccountConfigurations
from adyen.models.first import First
from adyen.models.last import Last
from adyen.models.link import Link
from adyen.models.mself import Self
from adyen.models.next import Next
from adyen.models.previous import Previous

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
            frequency_value=138,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    link=Link(
        first=First(
            href='href2',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        last=Last(
            href='href2',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        next=Next(
            href='href4',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        previous=Previous(
            href='href0',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        mself=Self(
            href='href0',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

