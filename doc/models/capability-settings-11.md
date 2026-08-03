
# Capability Settings 11

The settings that are allowed for the legal entity.

*This model accepts additional fields of type Any.*

## Structure

`CapabilitySettings11`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amount_per_industry` | [`Dict[str, PatchableAmountDto]`](../../doc/models/patchable-amount-dto.md) | Optional | The maximum amount a card holder can spend per industry. |
| `authorized_card_users` | `bool` | Optional | The number of card holders who can use the card. |
| `funding_source` | [`List[FundingSource]`](../../doc/models/funding-source.md) | Optional | The funding source of the card, for example **debit**. |
| `interval` | [`Interval`](../../doc/models/interval.md) | Optional | - |
| `max_amount` | [`MaxAmount`](../../doc/models/max-amount.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.capability_settings_11 import CapabilitySettings11
from adyen.models.funding_source import FundingSource
from adyen.models.interval import Interval
from adyen.models.max_amount import MaxAmount
from adyen.models.patchable_amount_dto import PatchableAmountDto

capability_settings_11 = CapabilitySettings11(
    amount_per_industry={
        'key0': PatchableAmountDto(
            currency='currency8',
            value=56,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        'key1': PatchableAmountDto(
            currency='currency8',
            value=56,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    },
    authorized_card_users=False,
    funding_source=[
        FundingSource.DEBIT
    ],
    interval=Interval.WEEKLY,
    max_amount=MaxAmount(
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

