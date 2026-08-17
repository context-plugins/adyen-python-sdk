
# Unreferenced 2

Settings for unreferenced refunds.

## Structure

`Unreferenced2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `enable_unreferenced_refunds` | `bool` | Optional | Indicates whether unreferenced refunds are enabled on the terminal.<br><br>> You're fully liable for losses resulting from fraudulent or duplicate unreferenced refunds. We recommend that you [set an unreferenced refund limit and a refund delay](https://docs.adyen.com/point-of-sale/basic-tapi-integration/refund-payment/unreferenced/#risk-with-unreferenced-refunds) to reduce this risk. |

## Example

```python
from adyen.models.unreferenced_2 import Unreferenced2

unreferenced_2 = Unreferenced2(
    enable_unreferenced_refunds=False
)
```

