
# Remediating Action

## Structure

`RemediatingAction`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `code` | `str` | Optional | The remediating action code. |
| `message` | `str` | Optional | A description of how you can resolve the verification error. |

## Example

```python
from adyen.models.remediating_action import RemediatingAction

remediating_action = RemediatingAction(
    code='code0',
    message='message8'
)
```

