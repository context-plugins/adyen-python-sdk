
# Delivery Timeframe

The estimated delivery time for the shopper to receive the goods.
Allowed values:

* `electronicDelivery`
* `sameDayShipping`
* `overnightShipping`
* `twoOrMoreDaysShipping`

## Enumeration

`DeliveryTimeframe`

## Fields

| Name |
|  --- |
| `ELECTRONICDELIVERY` |
| `SAMEDAYSHIPPING` |
| `OVERNIGHTSHIPPING` |
| `TWOORMOREDAYSSHIPPING` |

## Example

```python
from adyen.models.delivery_timeframe import DeliveryTimeframe

delivery_timeframe = DeliveryTimeframe.OVERNIGHTSHIPPING
```

