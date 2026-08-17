
# Token Requested Type 1 Enum

Type of token replacing the PAN of a payment card to identify the payment
mean of the customer. It allows, for a merchant, to use a token for a transaction
only or for a longer period.
Possible values:

* **Customer**
* **Transaction**

## Enumeration

`TokenRequestedType1Enum`

## Fields

| Name |
|  --- |
| `TRANSACTION` |
| `CUSTOMER` |

## Example

```python
from adyen.models.token_requested_type_1_enum import TokenRequestedType1Enum

token_requested_type_1 = TokenRequestedType1Enum.TRANSACTION
```

