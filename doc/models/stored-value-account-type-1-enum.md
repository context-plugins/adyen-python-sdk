
# Stored Value Account Type 1 Enum

Type of stored value account. Allows the distinction of the stored value instrument to access the stored value account.
Possible values:

* **GiftCard**
* **Other**
* **PhoneCard**

## Enumeration

`StoredValueAccountType1Enum`

## Fields

| Name |
|  --- |
| `GIFTCARD` |
| `PHONECARD` |
| `OTHER` |

## Example

```python
from adyen.models.stored_value_account_type_1_enum import StoredValueAccountType1Enum

stored_value_account_type_1 = StoredValueAccountType1Enum.GIFTCARD
```

