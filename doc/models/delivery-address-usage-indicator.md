
# Delivery Address Usage Indicator

Indicator for the length of time since this delivery address was first used.
Allowed values:

* thisTransaction
* lessThan30Days
* from30To60Days
* moreThan60Days

## Enumeration

`DeliveryAddressUsageIndicator`

## Fields

| Name |
|  --- |
| `THISTRANSACTION` |
| `LESSTHAN30DAYS` |
| `FROM30TO60DAYS` |
| `MORETHAN60DAYS` |

## Example

```python
from adyen.models.delivery_address_usage_indicator import DeliveryAddressUsageIndicator

delivery_address_usage_indicator = DeliveryAddressUsageIndicator.THISTRANSACTION
```

