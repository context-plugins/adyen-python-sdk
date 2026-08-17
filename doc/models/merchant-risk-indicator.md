
# Merchant Risk Indicator

## Structure

`MerchantRiskIndicator`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `address_match` | `bool` | Optional | Whether the chosen delivery address is identical to the billing address. |
| `delivery_address_indicator` | [`DeliveryAddressIndicatorEnum`](../../doc/models/delivery-address-indicator-enum.md) | Optional | Indicator regarding the delivery address.<br>Allowed values:<br><br>* `shipToBillingAddress`<br>* `shipToVerifiedAddress`<br>* `shipToNewAddress`<br>* `shipToStore`<br>* `digitalGoods`<br>* `goodsNotShipped`<br>* `other` |
| `delivery_email` | `str` | Optional | The delivery email address (for digital goods). |
| `delivery_email_address` | `str` | Optional | For Electronic delivery, the email address to which the merchandise was delivered. Maximum length: 254 characters.<br><br>**Constraints**: *Maximum Length*: `254` |
| `delivery_timeframe` | [`DeliveryTimeframeEnum`](../../doc/models/delivery-timeframe-enum.md) | Optional | The estimated delivery time for the shopper to receive the goods.<br>Allowed values:<br><br>* `electronicDelivery`<br>* `sameDayShipping`<br>* `overnightShipping`<br>* `twoOrMoreDaysShipping` |
| `gift_card_amount` | [`Amount7`](../../doc/models/amount-7.md) | Optional | For prepaid or gift card purchase, the purchase amount total of prepaid or gift card(s). |
| `gift_card_count` | `int` | Optional | For prepaid or gift card purchase, total count of individual prepaid or gift cards/codes purchased. |
| `gift_card_curr` | `str` | Optional | For prepaid or gift card purchase, [ISO 4217](https://www.iso.org/iso-4217-currency-codes.html) three-digit currency code of the gift card, other than those listed in Table A.5 of the EMVCo 3D Secure Protocol and Core Functions Specification. |
| `pre_order_date` | `datetime` | Optional | For pre-order purchases, the expected date this product will be available to the shopper. |
| `pre_order_purchase` | `bool` | Optional | Indicator for whether this transaction is for pre-ordering a product. |
| `pre_order_purchase_ind` | `str` | Optional | Indicates whether Cardholder is placing an order for merchandise with a future availability or release date. |
| `reorder_items` | `bool` | Optional | Indicator for whether the shopper has already purchased the same items in the past. |
| `reorder_items_ind` | `str` | Optional | Indicates whether the cardholder is reordering previously purchased merchandise. |
| `ship_indicator` | `str` | Optional | Indicates shipping method chosen for the transaction. |

## Example

```python
from adyen.models.delivery_address_indicator_enum import DeliveryAddressIndicatorEnum
from adyen.models.delivery_timeframe_enum import DeliveryTimeframeEnum
from adyen.models.merchant_risk_indicator import MerchantRiskIndicator

merchant_risk_indicator = MerchantRiskIndicator(
    address_match=False,
    delivery_address_indicator=DeliveryAddressIndicatorEnum.GOODSNOTSHIPPED,
    delivery_email='deliveryEmail2',
    delivery_email_address='deliveryEmailAddress2',
    delivery_timeframe=DeliveryTimeframeEnum.ELECTRONICDELIVERY
)
```

