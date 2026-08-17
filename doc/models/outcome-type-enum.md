
# Outcome Type Enum

The [outcome](https://docs.adyen.com/issuing/transaction-rules#outcome) that will be applied when a transaction meets the conditions of the rule.

Possible values:

* **hardBlock** (default): the transaction is declined.

* **scoreBased**: the transaction is assigned the `score` you specified. Adyen calculates the total score and if it exceeds 100, the transaction is declined. This value is not allowed when `requestType` is **bankTransfer**.

* **enforceSCA**: your user is prompted to verify their identity using [3D Secure authentication](https://docs.adyen.com/issuing/3d-secure/). If the authentication fails or times out, the transaction is declined. This value is only allowed when `requestType` is **authentication**.

## Enumeration

`OutcomeTypeEnum`

## Fields

| Name |
|  --- |
| `ENFORCESCA` |
| `HARDBLOCK` |
| `SCOREBASED` |
| `TIMEDBLOCK` |

## Example

```python
from adyen.models.outcome_type_enum import OutcomeTypeEnum

outcome_type = OutcomeTypeEnum.SCOREBASED
```

