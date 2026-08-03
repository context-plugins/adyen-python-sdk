
# Stored Value Transaction Type 1

Identification of operation to proceed on the stored value account or the stored value card.
Possible values:

* **Activate**
* **Duplicate**
* **Load**
* **Reserve**
* **Reverse**
* **Unload**

## Enumeration

`StoredValueTransactionType1`

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
from adyen.models.stored_value_transaction_type_1 import StoredValueTransactionType1

stored_value_transaction_type_1 = StoredValueTransactionType1.LOAD
```

