
# Capability Settings

## Structure

`CapabilitySettings`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amount_per_industry` | [`Dict[str, Amount17]`](../../doc/models/amount-17.md) | Optional | - |
| `authorized_card_users` | `bool` | Optional | - |
| `funding_source` | [`List[FundingSourceEnum]`](../../doc/models/funding-source-enum.md) | Optional | - |
| `interval` | [`IntervalEnum`](../../doc/models/interval-enum.md) | Optional | - |
| `max_amount` | [`Amount17`](../../doc/models/amount-17.md) | Optional | - |

## Example

```python
from adyen.models.amount_17 import Amount17
from adyen.models.capability_settings import CapabilitySettings
from adyen.models.funding_source_enum import FundingSourceEnum
from adyen.models.interval_enum import IntervalEnum

capability_settings = CapabilitySettings(
    amount_per_industry={
        'key0': Amount17(
            currency='currency8',
            value=56
        ),
        'key1': Amount17(
            currency='currency8',
            value=56
        ),
        'key2': Amount17(
            currency='currency8',
            value=56
        )
    },
    authorized_card_users=False,
    funding_source=[
        FundingSourceEnum.DEBIT,
        FundingSourceEnum.CREDIT
    ],
    interval=IntervalEnum.DAILY,
    max_amount=Amount17(
        currency='currency4',
        value=160
    )
)
```

