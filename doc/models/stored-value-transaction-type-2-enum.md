
# Stored Value Transaction Type 2 Enum

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

`StoredValueTransactionType2Enum`

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
from adyen.models.stored_value_transaction_type_2_enum import StoredValueTransactionType2Enum

stored_value_transaction_type_2 = StoredValueTransactionType2Enum.LOAD
```

