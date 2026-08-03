
# Stored Value Account Type 1

Type of stored value account. Allows the distinction of the stored value instrument to access the stored value account.
Possible values:

* **GiftCard**
* **Other**
* **PhoneCard**

## Enumeration

`StoredValueAccountType1`

## Fields

| Name |
|  --- |
| `GIFTCARD` |
| `PHONECARD` |
| `OTHER` |

## Example

```python
from adyen.models.stored_value_account_type_1 import StoredValueAccountType1

stored_value_account_type_1 = StoredValueAccountType1.GIFTCARD
```

