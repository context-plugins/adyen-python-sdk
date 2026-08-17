
# Payment Token

Surrogate of the PAN (Primary Account Number) of the payment card to
identify the payment mean of the customer. It allows, for a merchant, to identify
the customer.

## Structure

`PaymentToken`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `token_requested_type` | [`TokenRequestedType1Enum`](../../doc/models/token-requested-type-1-enum.md) | Required | Type of token replacing the PAN of a payment card to identify the payment<br>mean of the customer. It allows, for a merchant, to use a token for a transaction<br>only or for a longer period.<br>Possible values:<br><br>* **Customer**<br>* **Transaction** |
| `token_value` | `str` | Required | Payment token replacing the PAN of the payment card to identify the payment<br>mean of the customer.<br><br>**Constraints**: *Pattern*: `^.+$` |
| `expiry_date_time` | `datetime` | Optional | Expiry date and time. Limits the validity of a payment token. |

## Example

```python
import dateutil.parser

from adyen.models.payment_token import PaymentToken
from adyen.models.token_requested_type_1_enum import TokenRequestedType1Enum

payment_token = PaymentToken(
    token_requested_type=TokenRequestedType1Enum.TRANSACTION,
    token_value='TokenValue6',
    expiry_date_time=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
)
```

