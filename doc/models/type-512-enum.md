
# Type 512 Enum

The type of error.

Possible values:

* **invalidInput**
* **dataMissing**
* **pendingStatus**
* **rejected**
* **dataReview**

## Enumeration

`Type512Enum`

## Fields

| Name |
|  --- |
| `DATAMISSING` |
| `DATAREVIEW` |
| `INVALIDINPUT` |
| `PENDINGSTATUS` |
| `REJECTED` |

## Example

```python
from adyen.models.type_512_enum import Type512Enum

type_512 = Type512Enum.DATAMISSING
```

