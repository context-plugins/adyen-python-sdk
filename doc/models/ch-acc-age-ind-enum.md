
# Ch Acc Age Ind Enum

Length of time that the cardholder has had the account with the 3DS Requestor.
Allowed values:

* **01** — No account
* **02** — Created during this transaction
* **03** — Less than 30 days
* **04** — 30–60 days
* **05** — More than 60 days, Indicates the length of time since the cardholder’s account with the 3DS Requestor had a password change or account reset.
  Allowed values:
* **01** — No change
* **02** — Changed during this transaction
* **03** — Less than 30 days
* **04** — 30–60 days
* **05** — More than 60 days, Dimensions of the 3DS2 challenge window to be displayed to the cardholder.

Possible values:

* **01** - size of 250x400
* **02** - size of 390x400
* **03** - size of 500x600
* **04** - size of 600x400
* **05** - Fullscreen, Indicates the length of time that the payment account was enrolled in the cardholder’s account with the 3DS Requestor.
  Allowed values:
* **01** — No account (guest checkout)
* **02** — During this transaction
* **03** — Less than 30 days
* **04** — 30–60 days
* **05** — More than 60 days

## Enumeration

`ChAccAgeIndEnum`

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
from adyen.models.ch_acc_age_ind_enum import ChAccAgeIndEnum

ch_acc_age_ind = ChAccAgeIndEnum.ENUM_03
```

