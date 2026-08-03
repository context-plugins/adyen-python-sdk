
# Merchant Risk Indicator

*This model accepts additional fields of type Any.*

## Structure

`MerchantRiskIndicator`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `address_match` | `bool` | Optional | Whether the chosen delivery address is identical to the billing address. |
| `delivery_address_indicator` | [`DeliveryAddressIndicator`](../../doc/models/delivery-address-indicator.md) | Optional | - |
| `delivery_email` | `str` | Optional | The delivery email address (for digital goods). |
| `delivery_email_address` | `str` | Optional | For Electronic delivery, the email address to which the merchandise was delivered. Maximum length: 254 characters.<br><br>**Constraints**: *Maximum Length*: `254` |
| `delivery_timeframe` | [`DeliveryTimeframe`](../../doc/models/delivery-timeframe.md) | Optional | - |
| `gift_card_amount` | [`GiftCardAmount`](../../doc/models/gift-card-amount.md) | Optional | - |
| `gift_card_count` | `int` | Optional | For prepaid or gift card purchase, total count of individual prepaid or gift cards/codes purchased. |
| `gift_card_curr` | `str` | Optional | For prepaid or gift card purchase, [ISO 4217](https://www.iso.org/iso-4217-currency-codes.html) three-digit currency code of the gift card, other than those listed in Table A.5 of the EMVCo 3D Secure Protocol and Core Functions Specification. |
| `pre_order_date` | `datetime` | Optional | For pre-order purchases, the expected date this product will be available to the shopper. |
| `pre_order_purchase` | `bool` | Optional | Indicator for whether this transaction is for pre-ordering a product. |
| `pre_order_purchase_ind` | `str` | Optional | Indicates whether Cardholder is placing an order for merchandise with a future availability or release date. |
| `reorder_items` | `bool` | Optional | Indicator for whether the shopper has already purchased the same items in the past. |
| `reorder_items_ind` | `str` | Optional | Indicates whether the cardholder is reordering previously purchased merchandise. |
| `ship_indicator` | `str` | Optional | Indicates shipping method chosen for the transaction. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.delivery_address_indicator import DeliveryAddressIndicator
from adyen.models.delivery_timeframe import DeliveryTimeframe
from adyen.models.merchant_risk_indicator import MerchantRiskIndicator

merchant_risk_indicator = MerchantRiskIndicator(
    address_match=False,
    delivery_address_indicator=DeliveryAddressIndicator.GOODSNOTSHIPPED,
    delivery_email='deliveryEmail2',
    delivery_email_address='deliveryEmailAddress2',
    delivery_timeframe=DeliveryTimeframe.ELECTRONICDELIVERY,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

