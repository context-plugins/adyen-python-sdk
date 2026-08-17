
# Challenge Indicator Enum

Possibility to specify a preference for receiving a challenge from the issuer.
Allowed values:

* `noPreference`
* `requestNoChallenge`
* `requestChallenge`
* `requestChallengeAsMandate`

## Enumeration

`ChallengeIndicatorEnum`

## Fields

| Name |
|  --- |
| `NOPREFERENCE` |
| `REQUESTNOCHALLENGE` |
| `REQUESTCHALLENGE` |
| `REQUESTCHALLENGEASMANDATE` |

## Example

```python
from adyen.models.challenge_indicator_enum import ChallengeIndicatorEnum

challenge_indicator = ChallengeIndicatorEnum.REQUESTCHALLENGE
```

