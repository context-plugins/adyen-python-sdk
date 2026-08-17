
# Payment Method Issuer

## Structure

`PaymentMethodIssuer`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `disabled` | `bool` | Optional | A boolean value indicating whether this issuer is unavailable. Can be `true` whenever the issuer is offline.<br><br>**Default**: `False` |
| `id` | `str` | Required | The unique identifier of this issuer, to submit in requests to /payments. |
| `name` | `str` | Required | A localized name of the issuer. |

## Example

```python
from adyen.models.payment_method_issuer import PaymentMethodIssuer

payment_method_issuer = PaymentMethodIssuer(
    id='id8',
    name='name8',
    disabled=False
)
```

