
# Account Type 3

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

`AccountType3`

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
from adyen.models.account_type_3 import AccountType3

account_type_3 = AccountType3.CHECKING
```

