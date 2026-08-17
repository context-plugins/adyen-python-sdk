
# Addr Match 1 Enum

Indicates whether the cardholder shipping Address and cardholder billing address are the same. Allowed values:

* **Y** — Shipping Address matches Billing Address.
* **N** — Shipping Address does not match Billing Address.

## Enumeration

`AddrMatch1Enum`

## Fields

| Name |
|  --- |
| `Y` |
| `N` |

## Example

```python
from adyen.models.addr_match_1_enum import AddrMatch1Enum

addr_match_1 = AddrMatch1Enum.Y
```

