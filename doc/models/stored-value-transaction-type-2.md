
# Stored Value Transaction Type 2

Identification of operation to proceed on the stored value account or the stored value card.
Copy.
Possible values:

* **Activate**
* **Duplicate**
* **Load**
* **Reserve**
* **Reverse**
* **Unload**

## Enumeration

`StoredValueTransactionType2`

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
from adyen.models.stored_value_transaction_type_2 import StoredValueTransactionType2

stored_value_transaction_type_2 = StoredValueTransactionType2.LOAD
```

