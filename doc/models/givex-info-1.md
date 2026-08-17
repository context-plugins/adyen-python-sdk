
# Givex Info 1

Details to provide if `type` is **givex**.

## Structure

`GivexInfo1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `currency_code` | `str` | Required | The three-character ISO currency code, such as **EUR**. |
| `password` | `str` | Required | The password provided by the acquirer. |
| `payment_flow` | [`PaymentFlowEnum`](../../doc/models/payment-flow-enum.md) | Required | The sales channel used for the payment. |
| `username` | `str` | Required | The username provided by the acquirer. |

## Example

```python
from adyen.models.givex_info_1 import GivexInfo1
from adyen.models.payment_flow_enum import PaymentFlowEnum

givex_info_1 = GivexInfo1(
    currency_code='currencyCode2',
    password='password6',
    payment_flow=PaymentFlowEnum.ECOMMERCE,
    username='username8'
)
```

