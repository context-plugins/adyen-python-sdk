
# Challenge Window Size

Dimensions of the 3DS2 challenge window to be displayed to the cardholder.

Possible values:

* **01** - size of 250x400
* **02** - size of 390x400
* **03** - size of 500x600
* **04** - size of 600x400
* **05** - Fullscreen

## Enumeration

`ChallengeWindowSize`

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
from adyen.models.challenge_window_size import ChallengeWindowSize

challenge_window_size = ChallengeWindowSize.ENUM_03
```

