
# Account Supporting Entity Capability

## Structure

`AccountSupportingEntityCapability`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `allowed` | `bool` | Optional, Read-only | Indicates whether the supporting entity capability is allowed. Adyen sets this to **true** if the verification is successful and the account holder is permitted to use the capability. |
| `allowed_level` | [`AllowedLevelEnum`](../../doc/models/allowed-level-enum.md) | Optional, Read-only | The capability level that is allowed for the account holder.<br><br>Possible values: **notApplicable**, **low**, **medium**, **high**. |
| `enabled` | `bool` | Optional | Indicates whether the capability is enabled. If **false**, the capability is temporarily disabled for the account holder. |
| `id` | `str` | Optional, Read-only | The ID of the supporting entity. |
| `requested` | `bool` | Optional | Indicates whether the capability is requested. To check whether the account holder is permitted to use the capability, refer to the `allowed` field. |
| `requested_level` | [`RequestedLevelEnum`](../../doc/models/requested-level-enum.md) | Optional | The requested level of the capability. Some capabilities, such as those used in [card issuing](https://docs.adyen.com/issuing/add-capabilities#capability-levels), have different levels. Levels increase the capability, but also require additional checks and increased monitoring.<br><br>Possible values: **notApplicable**, **low**, **medium**, **high**. |
| `verification_status` | [`VerificationStatusEnum`](../../doc/models/verification-status-enum.md) | Optional, Read-only | The status of the verification checks for the supporting entity capability.<br><br>Possible values:<br><br>* **pending**: Adyen is running the verification.<br><br>* **invalid**: The verification failed. Check if the `errors` array contains more information.<br><br>* **valid**: The verification has been successfully completed.<br><br>* **rejected**: Adyen has verified the information, but found reasons to not allow the capability. |

## Example

```python
from adyen.models.account_supporting_entity_capability import AccountSupportingEntityCapability

account_supporting_entity_capability = AccountSupportingEntityCapability(
    enabled=False,
    requested=False
)
```

