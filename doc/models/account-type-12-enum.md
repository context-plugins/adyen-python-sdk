
# Account Type 12 Enum

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

`AccountType12Enum`

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
from adyen.models.account_type_12_enum import AccountType12Enum

account_type_12 = AccountType12Enum.CARDTOTALS
```

