
# US Instant Payout Address Requirement

## Structure

`USInstantPayoutAddressRequirement`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `description` | `str` | Optional | Specifies that you must provide complete street addresses for the party and counterParty for transactions greater than USD 3000. |
| `mtype` | `str` | Required, Constant | **usInstantPayoutAddressRequirement**<br><br>**Value**: `"usInstantPayoutAddressRequirement"` |

## Example

```python
from adyen.models.us_instant_payout_address_requirement import USInstantPayoutAddressRequirement

us_instant_payout_address_requirement = USInstantPayoutAddressRequirement(
    description='description8'
)
```

