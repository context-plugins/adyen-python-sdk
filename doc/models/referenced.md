
# Referenced

## Structure

`Referenced`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `enable_standalone_refunds` | `bool` | Optional | Indicates whether referenced refunds are enabled on the standalone terminal. |

## Example

```python
from adyen.models.referenced import Referenced

referenced = Referenced(
    enable_standalone_refunds=False
)
```

