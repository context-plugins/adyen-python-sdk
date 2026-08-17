
# Legal Entity Capability

## Structure

`LegalEntityCapability`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `allowed` | `bool` | Optional, Read-only | Indicates whether the capability is allowed. Adyen sets this to **true** if the verification is successful. |
| `allowed_level` | [`AllowedLevelEnum`](../../doc/models/allowed-level-enum.md) | Optional, Read-only | The capability level that is allowed for the legal entity.<br><br>Possible values: **notApplicable**, **low**, **medium**, **high**. |
| `allowed_settings` | [`CapabilitySettings11`](../../doc/models/capability-settings-11.md) | Optional | The settings that are allowed for the legal entity. |
| `requested` | `bool` | Optional, Read-only | Indicates whether the capability is requested. To check whether the legal entity is permitted to use the capability, refer to the `allowed` field. |
| `requested_level` | [`AllowedLevelEnum`](../../doc/models/allowed-level-enum.md) | Optional, Read-only | The requested level of the capability. Some capabilities, such as those used in [card issuing](https://docs.adyen.com/issuing/add-capabilities#capability-levels), have different levels. Levels increase the capability, but also require additional checks and increased monitoring.<br><br>Possible values: **notApplicable**, **low**, **medium**, **high**. |
| `requested_settings` | [`CapabilitySettings21`](../../doc/models/capability-settings-21.md) | Optional | The settings that are requested for the legal entity. |
| `transfer_instruments` | [`List[SupportingEntityCapability]`](../../doc/models/supporting-entity-capability.md) | Optional, Read-only | The capability status of transfer instruments associated with the legal entity. |
| `verification_status` | `str` | Optional, Read-only | The status of the verification checks for the capability.<br><br>Possible values:<br><br>* **pending**: Adyen is running the verification.<br><br>* **invalid**: The verification failed. Check if the `errors` array contains more information.<br><br>* **valid**: The verification has been successfully completed.<br><br>* **rejected**: Adyen has verified the information, but found reasons to not allow the capability. |

## Example

```python
from adyen.models.capability_settings_11 import CapabilitySettings11
from adyen.models.funding_source_enum import FundingSourceEnum
from adyen.models.interval_enum import IntervalEnum
from adyen.models.legal_entity_capability import LegalEntityCapability
from adyen.models.patchable_amount_dto import PatchableAmountDTO

legal_entity_capability = LegalEntityCapability(
    allowed_settings=CapabilitySettings11(
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
            FundingSourceEnum.CREDIT,
            FundingSourceEnum.DEBIT,
            FundingSourceEnum.PREPAID
        ],
        interval=IntervalEnum.DAILY,
        max_amount=PatchableAmountDTO(
            currency='currency4',
            value=160
        )
    )
)
```

