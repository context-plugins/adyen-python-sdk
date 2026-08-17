
# Requested Level Enum

The requested level of the capability. Some capabilities, such as those used in [card issuing](https://docs.adyen.com/issuing/add-capabilities#capability-levels), have different levels. Levels increase the capability, but also require additional checks and increased monitoring.

Possible values: **notApplicable**, **low**, **medium**, **high**.

## Enumeration

`RequestedLevelEnum`

## Fields

| Name |
|  --- |
| `HIGH` |
| `LOW` |
| `MEDIUM` |
| `NOTAPPLICABLE` |

## Example

```python
from adyen.models.requested_level_enum import RequestedLevelEnum

requested_level = RequestedLevelEnum.MEDIUM
```

