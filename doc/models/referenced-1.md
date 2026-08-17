
# Referenced 1

Settings for referenced refunds.

## Structure

`Referenced1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `enable_standalone_refunds` | `bool` | Optional | Indicates whether referenced refunds are enabled on the standalone terminal. |

## Example

```python
from adyen.models.referenced_1 import Referenced1

referenced_1 = Referenced1(
    enable_standalone_refunds=False
)
```

