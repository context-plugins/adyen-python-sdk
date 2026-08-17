
# Update Payment Link Request

## Structure

`UpdatePaymentLinkRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `status` | `str` | Required, Constant | Status of the payment link. Possible values:<br><br>* **expired**<br><br>**Value**: `"expired"` |

## Example

```python
from adyen.models.update_payment_link_request import UpdatePaymentLinkRequest

update_payment_link_request = UpdatePaymentLinkRequest()
```

