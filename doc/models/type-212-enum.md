
# Type 212 Enum

The type of error.

Possible values:

* **invalidInput**
* **dataMissing**
* **pendingStatus**
* **dataReview**

## Enumeration

`Type212Enum`

## Fields

| Name |
|  --- |
| `DATAMISSING` |
| `DATAREVIEW` |
| `INVALIDINPUT` |
| `PENDINGSTATUS` |

## Example

```python
from adyen.models.type_212_enum import Type212Enum

type_212 = Type212Enum.DATAMISSING
```

