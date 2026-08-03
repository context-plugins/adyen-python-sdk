
# Account Supporting Entity Capability

*This model accepts additional fields of type Any.*

## Structure

`AccountSupportingEntityCapability`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `allowed` | `bool` | Optional, Read-only | Indicates whether the supporting entity capability is allowed. Adyen sets this to **true** if the verification is successful and the account holder is permitted to use the capability. |
| `allowed_level` | [`AllowedLevel`](../../doc/models/allowed-level.md) | Optional, Read-only | - |
| `enabled` | `bool` | Optional | Indicates whether the capability is enabled. If **false**, the capability is temporarily disabled for the account holder. |
| `id` | `str` | Optional, Read-only | The ID of the supporting entity. |
| `requested` | `bool` | Optional | Indicates whether the capability is requested. To check whether the account holder is permitted to use the capability, refer to the `allowed` field. |
| `requested_level` | [`RequestedLevel`](../../doc/models/requested-level.md) | Optional | - |
| `verification_status` | [`VerificationStatus`](../../doc/models/verification-status.md) | Optional, Read-only | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.account_supporting_entity_capability import AccountSupportingEntityCapability
from adyen.models.allowed_level import AllowedLevel

account_supporting_entity_capability = AccountSupportingEntityCapability(
    allowed=False,
    allowed_level=AllowedLevel.MEDIUM,
    enabled=False,
    id='id8',
    requested=False,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

