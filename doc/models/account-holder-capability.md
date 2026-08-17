
# Account Holder Capability

## Structure

`AccountHolderCapability`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `allowed` | `bool` | Optional, Read-only | Indicates whether the capability is allowed. Adyen sets this to **true** if the verification is successful and the account holder is permitted to use the capability. |
| `allowed_level` | [`AllowedLevelEnum`](../../doc/models/allowed-level-enum.md) | Optional, Read-only | The capability level that is allowed for the account holder.<br><br>Possible values: **notApplicable**, **low**, **medium**, **high**. |
| `allowed_settings` | [`CapabilitySettings3`](../../doc/models/capability-settings-3.md) | Optional | A JSON object containing the settings that are allowed for the account holder. |
| `enabled` | `bool` | Optional | Indicates whether the capability is enabled. If **false**, the capability is temporarily disabled for the account holder. |
| `problems` | [`List[CapabilityProblem]`](../../doc/models/capability-problem.md) | Optional, Read-only | Contains verification errors and the actions that you can take to resolve them. |
| `requested` | `bool` | Optional | Indicates whether the capability is requested. To check whether the account holder is permitted to use the capability, refer to the `allowed` field. |
| `requested_level` | [`RequestedLevelEnum`](../../doc/models/requested-level-enum.md) | Optional | The requested level of the capability. Some capabilities, such as those used in [card issuing](https://docs.adyen.com/issuing/add-capabilities#capability-levels), have different levels. Levels increase the capability, but also require additional checks and increased monitoring.<br><br>Possible values: **notApplicable**, **low**, **medium**, **high**. |
| `requested_settings` | [`CapabilitySettings1`](../../doc/models/capability-settings-1.md) | Optional | A JSON object containing the settings that were requested for the account holder. |
| `transfer_instruments` | [`List[AccountSupportingEntityCapability]`](../../doc/models/account-supporting-entity-capability.md) | Optional, Read-only | Contains the status of the transfer instruments associated with this capability. |
| `verification_status` | [`VerificationStatusEnum`](../../doc/models/verification-status-enum.md) | Optional, Read-only | The status of the verification checks for the capability.<br><br>Possible values:<br><br>* **pending**: Adyen is running the verification.<br><br>* **invalid**: The verification failed. Check if the `errors` array contains more information.<br><br>* **valid**: The verification has been successfully completed.<br><br>* **rejected**: Adyen has verified the information, but found reasons to not allow the capability. |

## Example

```python
from adyen.models.account_holder_capability import AccountHolderCapability
from adyen.models.amount_17 import Amount17
from adyen.models.capability_settings_3 import CapabilitySettings3
from adyen.models.funding_source_enum import FundingSourceEnum
from adyen.models.interval_enum import IntervalEnum

account_holder_capability = AccountHolderCapability(
    allowed_settings=CapabilitySettings3(
        amount_per_industry={
            'key0': Amount17(
                currency='currency8',
                value=56
            ),
            'key1': Amount17(
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
        max_amount=Amount17(
            currency='currency4',
            value=160
        )
    ),
    enabled=False
)
```

