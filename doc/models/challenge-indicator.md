
# Challenge Indicator

Possibility to specify a preference for receiving a challenge from the issuer.
Allowed values:

* `noPreference`
* `requestNoChallenge`
* `requestChallenge`
* `requestChallengeAsMandate`

## Enumeration

`ChallengeIndicator`

## Fields

| Name |
|  --- |
| `NOPREFERENCE` |
| `REQUESTNOCHALLENGE` |
| `REQUESTCHALLENGE` |
| `REQUESTCHALLENGEASMANDATE` |

## Example

```python
from adyen.models.challenge_indicator import ChallengeIndicator

challenge_indicator = ChallengeIndicator.REQUESTCHALLENGE
```

