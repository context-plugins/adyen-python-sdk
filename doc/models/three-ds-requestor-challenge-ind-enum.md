
# Three DS Requestor Challenge Ind Enum

Indicates whether a challenge is requested for this transaction. Possible values:

* **01** — No preference
* **02** — No challenge requested
* **03** — Challenge requested (3DS Requestor preference)
* **04** — Challenge requested (Mandate)
* **05** — No challenge (transactional risk analysis is already performed)
* **06** — Data Only

## Enumeration

`ThreeDSRequestorChallengeIndEnum`

## Fields

| Name |
|  --- |
| `ENUM_01` |
| `ENUM_02` |
| `ENUM_03` |
| `ENUM_04` |
| `ENUM_05` |
| `ENUM_06` |

## Example

```python
from adyen.models.three_ds_requestor_challenge_ind_enum import ThreeDSRequestorChallengeIndEnum

three_ds_requestor_challenge_ind = ThreeDSRequestorChallengeIndEnum.ENUM_03
```

