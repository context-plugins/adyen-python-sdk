
# Ch Acc Change Ind

Length of time since the cardholder’s account information with the 3DS Requestor was last changed, including Billing or Shipping address, new payment account, or new user(s) added.
Allowed values:

* **01** — Changed during this transaction
* **02** — Less than 30 days
* **03** — 30–60 days
* **04** — More than 60 days

## Enumeration

`ChAccChangeInd`

## Fields

| Name |
|  --- |
| `ENUM_01` |
| `ENUM_02` |
| `ENUM_03` |
| `ENUM_04` |

## Example

```python
from adyen.models.ch_acc_change_ind import ChAccChangeInd

ch_acc_change_ind = ChAccChangeInd.ENUM_01
```

