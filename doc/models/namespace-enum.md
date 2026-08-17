
# Namespace Enum

The namespace that corresponds to the reason code.

Possible values:

* **ukFpsRejectionCode**
* **ukFpsReturnReasonCode**
* **usAchReturnReasonCode**
* **iso8583ResponseCode**

## Enumeration

`NamespaceEnum`

## Fields

| Name |
|  --- |
| `ISO8583RESPONSECODE` |
| `UKFPSREJECTIONCODE` |
| `UKFPSRETURNREASONCODE` |
| `USACHRETURNREASONCODE` |

## Example

```python
from adyen.models.namespace_enum import NamespaceEnum

namespace = NamespaceEnum.UKFPSRETURNREASONCODE
```

