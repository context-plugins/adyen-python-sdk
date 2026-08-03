
# Transaction Type

Identify the type of the transaction being authenticated.

## Enumeration

`TransactionType`

## Fields

| Name |
|  --- |
| `GOODSORSERVICEPURCHASE` |
| `CHECKACCEPTANCE` |
| `ACCOUNTFUNDING` |
| `QUASICASHTRANSACTION` |
| `PREPAIDACTIVATIONANDLOAD` |

## Example

```python
from adyen.models.transaction_type import TransactionType

transaction_type = TransactionType.ACCOUNTFUNDING
```

