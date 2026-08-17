
# Account Type 4 Enum

Type of cardholder account used for the transaction. Allows a cardholder to select the type of account used for the transaction.
Possible values:

* **Default**
* **Savings**
* **Checking**
* **CreditCard**
* **Universal**
* **Investment**
* **CardTotals**
* **EpurseCard**

## Enumeration

`AccountType4Enum`

## Fields

| Name |
|  --- |
| `DEFAULT` |
| `SAVINGS` |
| `CHECKING` |
| `CREDITCARD` |
| `UNIVERSAL` |
| `INVESTMENT` |
| `CARDTOTALS` |
| `EPURSECARD` |

## Example

```python
from adyen.models.account_type_4_enum import AccountType4Enum

account_type_4 = AccountType4Enum.CHECKING
```

