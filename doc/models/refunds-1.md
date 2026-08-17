
# Refunds 1

Settings for refunds.

## Structure

`Refunds1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `referenced` | [`Referenced1`](../../doc/models/referenced-1.md) | Optional | Settings for referenced refunds. |
| `unreferenced` | [`Unreferenced2`](../../doc/models/unreferenced-2.md) | Optional | Settings for unreferenced refunds. |

## Example

```python
from adyen.models.referenced_1 import Referenced1
from adyen.models.refunds_1 import Refunds1
from adyen.models.unreferenced_2 import Unreferenced2

refunds_1 = Refunds1(
    referenced=Referenced1(
        enable_standalone_refunds=False
    ),
    unreferenced=Unreferenced2(
        enable_unreferenced_refunds=False
    )
)
```

