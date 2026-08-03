
# Reason 11

The reason why the transfer failed Adyen's internal review.

Possible values:

- **refusedForRegulatoryReasons**: the transfer does not comply with Adyen's risk policy. For more information, [contact the Support Team](https://www.adyen.help/hc/en-us/requests/new).

## Enumeration

`Reason11`

## Fields

| Name |
|  --- |
| `REFUSEDFORREGULATORYREASONS` |

## Example

```python
from adyen.models.reason_11 import Reason11

reason_11 = Reason11.REFUSEDFORREGULATORYREASONS
```

