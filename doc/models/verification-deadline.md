
# Verification Deadline

*This model accepts additional fields of type Any.*

## Structure

`VerificationDeadline`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `capabilities` | [`List[Capability]`](../../doc/models/capability.md) | Required, Read-only | The names of the capabilities to be disallowed. |
| `entity_ids` | `List[str]` | Optional, Read-only | The unique identifiers of the bank account(s) that the deadline applies to |
| `expires_at` | `datetime` | Required, Read-only | The date that verification is due by before capabilities are disallowed. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from adyen.models.capability import Capability
from adyen.models.verification_deadline import VerificationDeadline

verification_deadline = VerificationDeadline(
    capabilities=[
        Capability.ACCEPTTRANSACTIONINRESTRICTEDCOUNTRIESCONSUMER
    ],
    expires_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    entity_ids=[
        'entityIds3'
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

