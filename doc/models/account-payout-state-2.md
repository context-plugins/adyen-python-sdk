
# Account Payout State 2

The payout state of the account holder.

*This model accepts additional fields of type Any.*

## Structure

`AccountPayoutState2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `allow_payout` | `bool` | Optional | Indicates whether payouts are allowed. This field is the overarching payout status, and is the aggregate of multiple conditions (e.g., KYC status, disabled flag, etc). If this field is false, no payouts will be permitted for any of the account holder's accounts. If this field is true, payouts will be permitted for any of the account holder's accounts. |
| `disable_reason` | `str` | Optional | The reason why payouts (to all of the account holder's accounts) have been disabled (by the platform). If the `disabled` field is true, this field can be used to explain why. |
| `disabled` | `bool` | Optional | Indicates whether payouts have been disabled (by the platform) for all of the account holder's accounts. A platform may enable and disable this field at their discretion. If this field is true, `allowPayout` will be false and no payouts will be permitted for any of the account holder's accounts. If this field is false, `allowPayout` may or may not be enabled, depending on other factors. |
| `not_allowed_reason` | `str` | Optional | The reason why payouts (to all of the account holder's accounts) have been disabled (by Adyen). If payouts have been disabled by Adyen, this field will explain why. If this field is blank, payouts have not been disabled by Adyen. |
| `payout_limit` | [`PayoutLimit`](../../doc/models/payout-limit.md) | Optional | - |
| `tier_number` | `int` | Optional | The payout tier that the account holder occupies. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.account_payout_state_2 import AccountPayoutState2
from adyen.models.payout_limit import PayoutLimit

account_payout_state_2 = AccountPayoutState2(
    allow_payout=False,
    disable_reason='disableReason6',
    disabled=False,
    not_allowed_reason='notAllowedReason6',
    payout_limit=PayoutLimit(
        currency='currency8',
        value=88,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

