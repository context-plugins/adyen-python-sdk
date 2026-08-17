
# Stored Value Transaction Type 1 Enum

Identification of operation to proceed on the stored value account or the stored value card.
Possible values:

* **Activate**
* **Duplicate**
* **Load**
* **Reserve**
* **Reverse**
* **Unload**

## Enumeration

`StoredValueTransactionType1Enum`

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
from adyen.models.stored_value_transaction_type_1_enum import StoredValueTransactionType1Enum

stored_value_transaction_type_1 = StoredValueTransactionType1Enum.LOAD
```

