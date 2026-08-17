
# Reason 11 Enum

The reason why the transfer failed Adyen's internal review.

Possible values:

- **refusedForRegulatoryReasons**: the transfer does not comply with Adyen's risk policy. For more information, [contact the Support Team](https://www.adyen.help/hc/en-us/requests/new).

## Enumeration

`Reason11Enum`

## Fields

| Name |
|  --- |
| `REFUSEDFORREGULATORYREASONS` |

## Example

```python
from adyen.models.reason_11_enum import Reason11Enum

reason_11 = Reason11Enum.REFUSEDFORREGULATORYREASONS
```

