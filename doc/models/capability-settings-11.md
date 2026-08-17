
# Capability Settings 11

The settings that are allowed for the legal entity.

## Structure

`CapabilitySettings11`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amount_per_industry` | [`Dict[str, PatchableAmountDTO]`](../../doc/models/patchable-amount-dto.md) | Optional | The maximum amount a card holder can spend per industry. |
| `authorized_card_users` | `bool` | Optional | The number of card holders who can use the card. |
| `funding_source` | [`List[FundingSourceEnum]`](../../doc/models/funding-source-enum.md) | Optional | The funding source of the card, for example **debit**. |
| `interval` | [`IntervalEnum`](../../doc/models/interval-enum.md) | Optional | The period when the rule conditions apply. |
| `max_amount` | [`PatchableAmountDTO`](../../doc/models/patchable-amount-dto.md) | Optional | The maximum amount a card holder can withdraw per day. |

## Example

```python
from adyen.models.capability_settings_11 import CapabilitySettings11
from adyen.models.funding_source_enum import FundingSourceEnum
from adyen.models.interval_enum import IntervalEnum
from adyen.models.patchable_amount_dto import PatchableAmountDTO

capability_settings_11 = CapabilitySettings11(
    amount_per_industry={
        'key0': PatchableAmountDTO(
            currency='currency8',
            value=56
        ),
        'key1': PatchableAmountDTO(
            currency='currency8',
            value=56
        )
    },
    authorized_card_users=False,
    funding_source=[
        FundingSourceEnum.DEBIT
    ],
    interval=IntervalEnum.WEEKLY,
    max_amount=PatchableAmountDTO(
        currency='currency4',
        value=160
    )
)
```

