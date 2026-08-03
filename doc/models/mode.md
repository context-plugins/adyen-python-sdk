
# Mode

Indicates the type of front end integration. Possible values:

* **embedded** (default): Drop-in or Components integration
* **hosted**: Hosted Checkout integration

## Enumeration

`Mode`

## Fields

| Name |
|  --- |
| `EMBEDDED` |
| `HOSTED` |

## Example

```python
from adyen.models.mode import Mode

mode = Mode.EMBEDDED
```

