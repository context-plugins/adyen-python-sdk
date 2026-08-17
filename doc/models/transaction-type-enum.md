
# Transaction Type Enum

Identify the type of the transaction being authenticated.

## Enumeration

`TransactionTypeEnum`

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
from adyen.models.transaction_type_enum import TransactionTypeEnum

transaction_type = TransactionTypeEnum.ACCOUNTFUNDING
```

