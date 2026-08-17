
# Pay at Table

## Structure

`PayAtTable`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `authentication_method` | [`AuthenticationMethodEnum`](../../doc/models/authentication-method-enum.md) | Optional | Allowed authentication methods: Magswipe, Manual Entry. |
| `enable_pay_at_table` | `bool` | Optional | Enable Pay at table. |
| `payment_instrument` | [`PaymentInstrumentEnum`](../../doc/models/payment-instrument-enum.md) | Optional | Sets the allowed payment instrument for Pay at table transactions.  Can be: **cash** or **card**. If not set, the terminal presents both options. |

## Example

```python
from adyen.models.authentication_method_enum import AuthenticationMethodEnum
from adyen.models.pay_at_table import PayAtTable
from adyen.models.payment_instrument_enum import PaymentInstrumentEnum

pay_at_table = PayAtTable(
    authentication_method=AuthenticationMethodEnum.MAGSWIPE,
    enable_pay_at_table=False,
    payment_instrument=PaymentInstrumentEnum.CASH
)
```

