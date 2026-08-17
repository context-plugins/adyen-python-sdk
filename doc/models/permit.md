
# Permit

## Structure

`Permit`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `partner_id` | `str` | Optional | Partner ID (when using the permit-per-partner token sharing model). |
| `profile_reference` | `str` | Optional | The profile to apply to this permit (when using the shared permits model). |
| `restriction` | [`PermitRestriction2`](../../doc/models/permit-restriction-2.md) | Optional | Permit level restriction overrides. |
| `result_key` | `str` | Optional | The key to link permit requests to permit results. |
| `valid_till_date` | `datetime` | Optional | The expiry date for this permit. |

## Example

```python
import dateutil.parser

from adyen.models.amount import Amount
from adyen.models.permit import Permit
from adyen.models.permit_restriction_2 import PermitRestriction2

permit = Permit(
    partner_id='partnerId4',
    profile_reference='profileReference6',
    restriction=PermitRestriction2(
        max_amount=Amount(
            currency='currency4',
            value=160
        ),
        single_transaction_limit=Amount(
            currency='currency8',
            value=122
        ),
        single_use=False
    ),
    result_key='resultKey0',
    valid_till_date=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
)
```

