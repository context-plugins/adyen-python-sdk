
# Payment Validations

## Structure

`PaymentValidations`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | [`Name6`](../../doc/models/name-6.md) | Optional | - |

## Example

```python
from adyen.models.name_6 import Name6
from adyen.models.payment_validations import PaymentValidations

payment_validations = PaymentValidations(
    name=Name6(
        status='status2'
    )
)
```

