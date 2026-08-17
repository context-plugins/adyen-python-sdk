
# Balance Platform

## Structure

`BalancePlatform`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `description` | `str` | Optional | Your description of the balance platform.<br><br>**Constraints**: *Maximum Length*: `300` |
| `id` | `str` | Required | The unique identifier of the balance platform. |
| `status` | `str` | Optional | The status of the balance platform.<br><br>Possible values: **Active**, **Inactive**, **Closed**, **Suspended**. |

## Example

```python
from adyen.models.balance_platform import BalancePlatform

balance_platform = BalancePlatform(
    id='id6',
    description='description6',
    status='status8'
)
```

