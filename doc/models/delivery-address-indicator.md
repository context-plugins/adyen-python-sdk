
# Delivery Address Indicator

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

`DeliveryAddressIndicator`

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
from adyen.models.delivery_address_indicator import DeliveryAddressIndicator

delivery_address_indicator = DeliveryAddressIndicator.SHIPTONEWADDRESS
```

