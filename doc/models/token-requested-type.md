
# Token Requested Type

Type of token replacing the PAN of a payment card to identify the payment mean of the customer. It allows, for a merchant, to use a token for a transaction only or for a longer period.
Possible values:

* **Transaction**
* **Customer**

## Enumeration

`TokenRequestedType`

## Fields

| Name |
|  --- |
| `TRANSACTION` |
| `CUSTOMER` |

## Example

```python
from adyen.models.token_requested_type import TokenRequestedType

token_requested_type = TokenRequestedType.TRANSACTION
```

