
# Stored Value Transaction Type Enum

Possible values:

* **Reserve**
* **Activate**
* **Load**
* **Unload**
* **Reverse**
* **Duplicate**

## Enumeration

`StoredValueTransactionTypeEnum`

## Fields

| Name |
|  --- |
| `RESERVE` |
| `ACTIVATE` |
| `LOAD` |
| `UNLOAD` |
| `REVERSE` |
| `DUPLICATE` |

## Example

```python
from adyen.models.stored_value_transaction_type_enum import StoredValueTransactionTypeEnum

stored_value_transaction_type = StoredValueTransactionTypeEnum.LOAD
```

