
# Ch Acc Age Ind

Length of time that the cardholder has had the account with the 3DS Requestor.
Allowed values:

* **01** — No account
* **02** — Created during this transaction
* **03** — Less than 30 days
* **04** — 30–60 days
* **05** — More than 60 days

## Enumeration

`ChAccAgeInd`

## Fields

| Name |
|  --- |
| `ENUM_01` |
| `ENUM_02` |
| `ENUM_03` |
| `ENUM_04` |
| `ENUM_05` |

## Example

```python
from adyen.models.ch_acc_age_ind import ChAccAgeInd

ch_acc_age_ind = ChAccAgeInd.ENUM_03
```

