
# Validate Shopper Id Request

## Structure

`ValidateShopperIdRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `merchant_account` | `str` | Required | The merchant account identifier, with which you want to process the transaction.<br><br>**Constraints**: *Minimum Length*: `0`, *Maximum Length*: `1000` |
| `payment_method` | [`ShopperIdPaymentMethod1`](../../doc/models/shopper-id-payment-method-1.md) | Required | paymentMethod |
| `shopper_email` | `str` | Optional | **Constraints**: *Minimum Length*: `0`, *Maximum Length*: `300` |
| `shopper_ip` | `str` | Optional | **Constraints**: *Minimum Length*: `0`, *Maximum Length*: `15` |
| `shopper_reference` | `str` | Optional | **Constraints**: *Minimum Length*: `0`, *Maximum Length*: `256` |

## Example

```python
from adyen.models.shopper_id_payment_method_1 import ShopperIdPaymentMethod1
from adyen.models.validate_shopper_id_request import ValidateShopperIdRequest

validate_shopper_id_request = ValidateShopperIdRequest(
    merchant_account='merchantAccount0',
    payment_method=ShopperIdPaymentMethod1(
        mtype='ShopperIdPaymentMethod1'
    ),
    shopper_email='shopperEmail8',
    shopper_ip='shopperIP6',
    shopper_reference='shopperReference6'
)
```

