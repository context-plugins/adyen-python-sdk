
# Paypal Update Order Request

## Structure

`PaypalUpdateOrderRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amount` | [`Amount44`](../../doc/models/amount-44.md) | Optional | The updated final payment amount. This amount is the item total plus the shipping costs of the selected `deliveryMethod`. |
| `delivery_address` | [`DeliveryAddress5`](../../doc/models/delivery-address-5.md) | Optional | The delivery address for this order. |
| `delivery_methods` | [`List[DeliveryMethod]`](../../doc/models/delivery-method.md) | Optional | The list of new delivery methods and the cost of each. |
| `discount_amount` | [`Amount45`](../../doc/models/amount-45.md) | Optional | The discount amount for this order. |
| `payment_data` | `str` | Optional | The `paymentData` from the client side. This value changes every time you make a `/paypal/updateOrder` request. |
| `psp_reference` | `str` | Optional | The original `pspReference` from the `/payments` response. |
| `session_id` | `str` | Optional | The original `sessionId` from the `/sessions` response. |
| `shipping_amount` | [`Amount46`](../../doc/models/amount-46.md) | Optional | The shipping amount for this order. |
| `tax_total` | [`TaxTotal2`](../../doc/models/tax-total-2.md) | Optional | Total tax amount from the order. |

## Example

```python
from adyen.models.amount_24 import Amount24
from adyen.models.amount_44 import Amount44
from adyen.models.amount_45 import Amount45
from adyen.models.delivery_address_5 import DeliveryAddress5
from adyen.models.delivery_method import DeliveryMethod
from adyen.models.paypal_update_order_request import PaypalUpdateOrderRequest
from adyen.models.type_21_enum import Type21Enum

paypal_update_order_request = PaypalUpdateOrderRequest(
    amount=Amount44(
        currency='currency2',
        value=110
    ),
    delivery_address=DeliveryAddress5(
        city='city4',
        country='country0',
        house_number_or_name='houseNumberOrName4',
        postal_code='postalCode2',
        street='street6',
        first_name='firstName8',
        last_name='lastName0',
        state_or_province='stateOrProvince6'
    ),
    delivery_methods=[
        DeliveryMethod(
            amount=Amount24(
                currency='currency2',
                value=110
            ),
            description='description6',
            reference='reference2',
            selected=False,
            mtype=Type21Enum.SHIPPING
        ),
        DeliveryMethod(
            amount=Amount24(
                currency='currency2',
                value=110
            ),
            description='description6',
            reference='reference2',
            selected=False,
            mtype=Type21Enum.SHIPPING
        ),
        DeliveryMethod(
            amount=Amount24(
                currency='currency2',
                value=110
            ),
            description='description6',
            reference='reference2',
            selected=False,
            mtype=Type21Enum.SHIPPING
        )
    ],
    discount_amount=Amount45(
        currency='currency8',
        value=168
    ),
    payment_data='paymentData2'
)
```

