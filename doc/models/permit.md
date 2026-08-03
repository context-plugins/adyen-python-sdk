
# Permit

*This model accepts additional fields of type Any.*

## Structure

`Permit`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `partner_id` | `str` | Optional | Partner ID (when using the permit-per-partner token sharing model). |
| `profile_reference` | `str` | Optional | The profile to apply to this permit (when using the shared permits model). |
| `restriction` | [`PermitRestriction`](../../doc/models/permit-restriction.md) | Optional | - |
| `result_key` | `str` | Optional | The key to link permit requests to permit results. |
| `valid_till_date` | `datetime` | Optional | The expiry date for this permit. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from adyen.models.max_amount_3 import MaxAmount3
from adyen.models.permit import Permit
from adyen.models.permit_restriction import PermitRestriction
from adyen.models.single_transaction_limit import SingleTransactionLimit

permit = Permit(
    partner_id='partnerId4',
    profile_reference='profileReference6',
    restriction=PermitRestriction(
        max_amount=MaxAmount3(
            currency='currency4',
            value=160,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        single_transaction_limit=SingleTransactionLimit(
            currency='currency8',
            value=122,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        single_use=False,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    result_key='resultKey0',
    valid_till_date=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

