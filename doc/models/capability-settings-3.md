
# Capability Settings 3

A JSON object containing the settings that are allowed for the account holder.

*This model accepts additional fields of type Any.*

## Structure

`CapabilitySettings3`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amount_per_industry` | [`Dict[str, Amount3]`](../../doc/models/amount-3.md) | Optional | - |
| `authorized_card_users` | `bool` | Optional | - |
| `funding_source` | [`List[FundingSource]`](../../doc/models/funding-source.md) | Optional | - |
| `interval` | [`Interval`](../../doc/models/interval.md) | Optional | The period when the rule conditions apply. |
| `max_amount` | [`Amount3`](../../doc/models/amount-3.md) | Optional | The amount that must be pushed out or pulled in. You can configure either `sweepAmount` or `targetAmount`, not both. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.amount_3 import Amount3
from adyen.models.capability_settings_3 import CapabilitySettings3
from adyen.models.funding_source import FundingSource
from adyen.models.interval import Interval

capability_settings_3 = CapabilitySettings3(
    amount_per_industry={
        'key0': Amount3(
            currency='currency8',
            value=56,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    },
    authorized_card_users=False,
    funding_source=[
        FundingSource.DEBIT,
        FundingSource.CREDIT
    ],
    interval=Interval.MONTHLY,
    max_amount=Amount3(
        currency='currency4',
        value=160,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

