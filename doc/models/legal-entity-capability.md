
# Legal Entity Capability

*This model accepts additional fields of type Any.*

## Structure

`LegalEntityCapability`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `allowed` | `bool` | Optional, Read-only | Indicates whether the capability is allowed. Adyen sets this to **true** if the verification is successful. |
| `allowed_level` | [`AllowedLevel`](../../doc/models/allowed-level.md) | Optional, Read-only | - |
| `allowed_settings` | [`CapabilitySettings2`](../../doc/models/capability-settings-2.md) | Optional | - |
| `requested` | `bool` | Optional, Read-only | Indicates whether the capability is requested. To check whether the legal entity is permitted to use the capability, refer to the `allowed` field. |
| `requested_level` | [`AllowedLevel`](../../doc/models/allowed-level.md) | Optional, Read-only | - |
| `requested_settings` | [`CapabilitySettings2`](../../doc/models/capability-settings-2.md) | Optional | - |
| `transfer_instruments` | [`List[SupportingEntityCapability]`](../../doc/models/supporting-entity-capability.md) | Optional, Read-only | The capability status of transfer instruments associated with the legal entity. |
| `verification_status` | `str` | Optional, Read-only | The status of the verification checks for the capability.<br><br>Possible values:<br><br>* **pending**: Adyen is running the verification.<br><br>* **invalid**: The verification failed. Check if the `errors` array contains more information.<br><br>* **valid**: The verification has been successfully completed.<br><br>* **rejected**: Adyen has verified the information, but found reasons to not allow the capability. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.allowed_level import AllowedLevel
from adyen.models.capability_settings_2 import CapabilitySettings2
from adyen.models.funding_source import FundingSource
from adyen.models.interval import Interval
from adyen.models.legal_entity_capability import LegalEntityCapability
from adyen.models.max_amount import MaxAmount
from adyen.models.patchable_amount_dto import PatchableAmountDto

legal_entity_capability = LegalEntityCapability(
    allowed=False,
    allowed_level=AllowedLevel.HIGH,
    allowed_settings=CapabilitySettings2(
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
            FundingSource.CREDIT,
            FundingSource.DEBIT,
            FundingSource.PREPAID
        ],
        interval=Interval.DAILY,
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
    ),
    requested=False,
    requested_level=AllowedLevel.HIGH,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

