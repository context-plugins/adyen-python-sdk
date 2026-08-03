
# Include Mode

Indicates whether the specified `eventType` is sent to your webhook endpoint.
Possible values:

* **INCLUDE**: Send the specified `eventType`.
* **EXCLUDE**: Send all event types except the specified `eventType` and other event types with the `includeMode` set to **EXCLUDE**.

## Enumeration

`IncludeMode`

## Fields

| Name |
|  --- |
| `EXCLUDE` |
| `INCLUDE` |

## Example

```python
from adyen.models.include_mode import IncludeMode

include_mode = IncludeMode.EXCLUDE
```

