
# Namespace

The namespace that corresponds to the reason code.

Possible values:

* **ukFpsRejectionCode**
* **ukFpsReturnReasonCode**
* **usAchReturnReasonCode**
* **iso8583ResponseCode**

## Enumeration

`Namespace`

## Fields

| Name |
|  --- |
| `ISO8583RESPONSECODE` |
| `UKFPSREJECTIONCODE` |
| `UKFPSRETURNREASONCODE` |
| `USACHRETURNREASONCODE` |

## Example

```python
from adyen.models.namespace import Namespace

namespace = Namespace.UKFPSRETURNREASONCODE
```

