
# Type 59

The type of error.

Possible values:

* **invalidInput**
* **dataMissing**
* **pendingStatus**
* **rejected**
* **dataReview**

## Enumeration

`Type59`

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
from adyen.models.type_59 import Type59

type_59 = Type59.PENDINGSTATUS
```

