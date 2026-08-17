
# Givex Info

## Structure

`GivexInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `currency_code` | `str` | Required | The three-character ISO currency code, such as **EUR**. |
| `password` | `str` | Required | The password provided by the acquirer. |
| `payment_flow` | [`PaymentFlowEnum`](../../doc/models/payment-flow-enum.md) | Required | The sales channel used for the payment. |
| `username` | `str` | Required | The username provided by the acquirer. |

## Example

```python
from adyen.models.givex_info import GivexInfo
from adyen.models.payment_flow_enum import PaymentFlowEnum

givex_info = GivexInfo(
    currency_code='currencyCode0',
    password='password4',
    payment_flow=PaymentFlowEnum.ECOMMERCE,
    username='username0'
)
```

