
# Balance Platform

*This model accepts additional fields of type Any.*

## Structure

`BalancePlatform`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `description` | `str` | Optional | Your description of the balance platform.<br><br>**Constraints**: *Maximum Length*: `300` |
| `id` | `str` | Required | The unique identifier of the balance platform. |
| `status` | `str` | Optional | The status of the balance platform.<br><br>Possible values: **Active**, **Inactive**, **Closed**, **Suspended**. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.balance_platform import BalancePlatform

balance_platform = BalancePlatform(
    id='id6',
    description='description6',
    status='status8',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

