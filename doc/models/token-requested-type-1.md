
# Token Requested Type 1

Type of token replacing the PAN of a payment card to identify the payment
mean of the customer. It allows, for a merchant, to use a token for a transaction
only or for a longer period.
Possible values:

* **Customer**
* **Transaction**

## Enumeration

`TokenRequestedType1`

## Fields

| Name |
|  --- |
| `TRANSACTION` |
| `CUSTOMER` |

## Example

```python
from adyen.models.token_requested_type_1 import TokenRequestedType1

token_requested_type_1 = TokenRequestedType1.TRANSACTION
```

