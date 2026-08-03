
# Stored Value Transaction Type

Possible values:

* **Reserve**
* **Activate**
* **Load**
* **Unload**
* **Reverse**
* **Duplicate**

## Enumeration

`StoredValueTransactionType`

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
from adyen.models.stored_value_transaction_type import StoredValueTransactionType

stored_value_transaction_type = StoredValueTransactionType.LOAD
```

