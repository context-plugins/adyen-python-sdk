
# Delivery Address Indicator Enum

Indicator regarding the delivery address.
Allowed values:

* `shipToBillingAddress`
* `shipToVerifiedAddress`
* `shipToNewAddress`
* `shipToStore`
* `digitalGoods`
* `goodsNotShipped`
* `other`

## Enumeration

`DeliveryAddressIndicatorEnum`

## Fields

| Name |
|  --- |
| `SHIPTOBILLINGADDRESS` |
| `SHIPTOVERIFIEDADDRESS` |
| `SHIPTONEWADDRESS` |
| `SHIPTOSTORE` |
| `DIGITALGOODS` |
| `GOODSNOTSHIPPED` |
| `OTHER` |

## Example

```python
from adyen.models.delivery_address_indicator_enum import DeliveryAddressIndicatorEnum

delivery_address_indicator = DeliveryAddressIndicatorEnum.SHIPTONEWADDRESS
```

