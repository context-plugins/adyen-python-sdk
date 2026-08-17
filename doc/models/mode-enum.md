
# Mode Enum

Indicates the type of front end integration. Possible values:

* **embedded** (default): Drop-in or Components integration
* **hosted**: Hosted Checkout integration

## Enumeration

`ModeEnum`

## Fields

| Name |
|  --- |
| `EMBEDDED` |
| `HOSTED` |

## Example

```python
from adyen.models.mode_enum import ModeEnum

mode = ModeEnum.EMBEDDED
```

