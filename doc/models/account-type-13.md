
# Account Type 13

Type of cardholder account used for the transaction. Allows a cardholder to select the type of account used for the transaction.
Possible values:

* **CardTotals**
* **Checking**
* **CreditCard**
* **Default**
* **EpurseCard**
* **Investment**
* **Savings**
* **Universal**

## Enumeration

`AccountType13`

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
from adyen.models.account_type_13 import AccountType13

account_type_13 = AccountType13.UNIVERSAL
```

