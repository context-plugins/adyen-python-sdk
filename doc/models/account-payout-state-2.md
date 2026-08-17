
# Account Payout State 2

The payout state of the account holder.

## Structure

`AccountPayoutState2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `allow_payout` | `bool` | Optional | Indicates whether payouts are allowed. This field is the overarching payout status, and is the aggregate of multiple conditions (e.g., KYC status, disabled flag, etc). If this field is false, no payouts will be permitted for any of the account holder's accounts. If this field is true, payouts will be permitted for any of the account holder's accounts. |
| `disable_reason` | `str` | Optional | The reason why payouts (to all of the account holder's accounts) have been disabled (by the platform). If the `disabled` field is true, this field can be used to explain why. |
| `disabled` | `bool` | Optional | Indicates whether payouts have been disabled (by the platform) for all of the account holder's accounts. A platform may enable and disable this field at their discretion. If this field is true, `allowPayout` will be false and no payouts will be permitted for any of the account holder's accounts. If this field is false, `allowPayout` may or may not be enabled, depending on other factors. |
| `not_allowed_reason` | `str` | Optional | The reason why payouts (to all of the account holder's accounts) have been disabled (by Adyen). If payouts have been disabled by Adyen, this field will explain why. If this field is blank, payouts have not been disabled by Adyen. |
| `payout_limit` | [`Amount`](../../doc/models/amount.md) | Optional | The maximum amount that payouts are limited to. Only applies if payouts are allowed but limited. |
| `tier_number` | `int` | Optional | The payout tier that the account holder occupies. |

## Example

```python
from adyen.models.account_payout_state_2 import AccountPayoutState2
from adyen.models.amount import Amount

account_payout_state_2 = AccountPayoutState2(
    allow_payout=False,
    disable_reason='disableReason6',
    disabled=False,
    not_allowed_reason='notAllowedReason6',
    payout_limit=Amount(
        currency='currency8',
        value=88
    )
)
```

