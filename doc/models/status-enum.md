
# Status Enum

Informs you if the name validation was performed. Possible values:

**performed**, **notPerformed**, **notSupported**

## Enumeration

`StatusEnum`

## Fields

| Name |
|  --- |
| `NOTPERFORMED` |
| `NOTSUPPORTED` |
| `PERFORMED` |

## Example

```python
from adyen.models.status_enum import StatusEnum

status = StatusEnum.PERFORMED
```

