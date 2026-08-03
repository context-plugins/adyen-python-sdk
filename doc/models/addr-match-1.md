
# Addr Match 1

Indicates whether the cardholder shipping Address and cardholder billing address are the same. Allowed values:

* **Y** — Shipping Address matches Billing Address.
* **N** — Shipping Address does not match Billing Address.

## Enumeration

`AddrMatch1`

## Fields

| Name |
|  --- |
| `Y` |
| `N` |

## Example

```python
from adyen.models.addr_match_1 import AddrMatch1

addr_match_1 = AddrMatch1.Y
```

