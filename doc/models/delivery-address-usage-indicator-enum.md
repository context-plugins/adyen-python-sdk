
# Delivery Address Usage Indicator Enum

Indicator for the length of time since this delivery address was first used.
Allowed values:

* thisTransaction
* lessThan30Days
* from30To60Days
* moreThan60Days

## Enumeration

`DeliveryAddressUsageIndicatorEnum`

## Fields

| Name |
|  --- |
| `THISTRANSACTION` |
| `LESSTHAN30DAYS` |
| `FROM30TO60DAYS` |
| `MORETHAN60DAYS` |

## Example

```python
from adyen.models.delivery_address_usage_indicator_enum import DeliveryAddressUsageIndicatorEnum

delivery_address_usage_indicator = DeliveryAddressUsageIndicatorEnum.THISTRANSACTION
```

