
# Payment Token 1

Surrogate of the PAN (Primary Account Number) of the payment card to identify the payment mean of the customer. It allows, for a merchant, to identify the customer.
Restriction of product payable by a card.

## Structure

`PaymentToken1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `token_requested_type` | [`TokenRequestedType1Enum`](../../doc/models/token-requested-type-1-enum.md) | Required | Type of token replacing the PAN of a payment card to identify the payment<br>mean of the customer. It allows, for a merchant, to use a token for a transaction<br>only or for a longer period.<br>Possible values:<br><br>* **Customer**<br>* **Transaction** |
| `token_value` | `str` | Required | Payment token replacing the PAN of the payment card to identify the payment<br>mean of the customer.<br><br>**Constraints**: *Pattern*: `^.+$` |
| `expiry_date_time` | `datetime` | Optional | Expiry date and time. Limits the validity of a payment token. |

## Example

```python
import dateutil.parser

from adyen.models.payment_token_1 import PaymentToken1
from adyen.models.token_requested_type_1_enum import TokenRequestedType1Enum

payment_token_1 = PaymentToken1(
    token_requested_type=TokenRequestedType1Enum.TRANSACTION,
    token_value='TokenValue2',
    expiry_date_time=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
)
```

