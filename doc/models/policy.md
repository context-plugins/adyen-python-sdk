
# Policy

*This model accepts additional fields of type Any.*

## Structure

`Policy`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `resources` | [`List[Resource]`](../../doc/models/resource.md) | Optional | An object containing the type and the unique identifier of the user of the component.<br><br>For [Onboarding components](https://docs.adyen.com/platforms/onboard-users/components), this is the ID of the legal entity that has a contractual relationship with your platform. For sole proprietorships, use the ID of the legal entity of the individual owner.<br><br>For [Platform Experience components](https://docs.adyen.com/platforms/build-user-dashboards), this is the ID of the account holder that is associated with the balance account shown in the component.<br><br>**Constraints**: *Unique Items Required* |
| `roles` | `List[str]` | Optional | The name of the role required to use the component.<br><br>**Constraints**: *Unique Items Required* |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.policy import Policy
from adyen.models.resource import Resource

policy = Policy(
    resources=[
        Resource(
            mtype='Resource',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    roles=[
        'roles8'
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

