
# Paypal Update Order Request

*This model accepts additional fields of type Any.*

## Structure

`PaypalUpdateOrderRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amount` | [`Amount16`](../../doc/models/amount-16.md) | Optional | - |
| `delivery_address` | [`DeliveryAddress1`](../../doc/models/delivery-address-1.md) | Optional | - |
| `delivery_methods` | [`List[DeliveryMethod]`](../../doc/models/delivery-method.md) | Optional | The list of new delivery methods and the cost of each. |
| `discount_amount` | [`DiscountAmount`](../../doc/models/discount-amount.md) | Optional | - |
| `payment_data` | `str` | Optional | The `paymentData` from the client side. This value changes every time you make a `/paypal/updateOrder` request. |
| `psp_reference` | `str` | Optional | The original `pspReference` from the `/payments` response. |
| `session_id` | `str` | Optional | The original `sessionId` from the `/sessions` response. |
| `shipping_amount` | [`ShippingAmount`](../../doc/models/shipping-amount.md) | Optional | - |
| `tax_total` | [`TaxTotal`](../../doc/models/tax-total.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.amount_16 import Amount16
from adyen.models.delivery_address_1 import DeliveryAddress1
from adyen.models.delivery_method import DeliveryMethod
from adyen.models.discount_amount import DiscountAmount
from adyen.models.paypal_update_order_request import PaypalUpdateOrderRequest
from adyen.models.type_211 import Type211

paypal_update_order_request = PaypalUpdateOrderRequest(
    amount=Amount16(
        currency='currency2',
        value=110,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    delivery_address=DeliveryAddress1(
        city='city4',
        country='country0',
        house_number_or_name='houseNumberOrName4',
        postal_code='postalCode2',
        street='street6',
        first_name='firstName8',
        last_name='lastName0',
        state_or_province='stateOrProvince6',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    delivery_methods=[
        DeliveryMethod(
            amount=Amount16(
                currency='currency2',
                value=110,
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            description='description6',
            reference='reference2',
            selected=False,
            mtype=Type211.SHIPPING,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        DeliveryMethod(
            amount=Amount16(
                currency='currency2',
                value=110,
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            description='description6',
            reference='reference2',
            selected=False,
            mtype=Type211.SHIPPING,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        DeliveryMethod(
            amount=Amount16(
                currency='currency2',
                value=110,
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            description='description6',
            reference='reference2',
            selected=False,
            mtype=Type211.SHIPPING,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    discount_amount=DiscountAmount(
        currency='currency8',
        value=168,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    payment_data='paymentData2',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

