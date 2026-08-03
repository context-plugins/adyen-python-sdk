
# Us Instant Payout Address Requirement

*This model accepts additional fields of type Any.*

## Structure

`UsInstantPayoutAddressRequirement`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `description` | `str` | Optional | Specifies that you must provide complete street addresses for the party and counterParty for transactions greater than USD 3000. |
| `mtype` | [`Type373`](../../doc/models/type-373.md) | Required | **usInstantPayoutAddressRequirement** |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.type_373 import Type373
from adyen.models.us_instant_payout_address_requirement import UsInstantPayoutAddressRequirement

us_instant_payout_address_requirement = UsInstantPayoutAddressRequirement(
    mtype=Type373.USINSTANTPAYOUTADDRESSREQUIREMENT,
    description='description8',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

