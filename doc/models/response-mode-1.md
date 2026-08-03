
# Response Mode 1

Message response awaited by the initiator of the Request. Allows various types and synchronisation of requests for Print or Sound.
Possible values:

* **Immediate**
* **NotRequired**
* **PrintEnd**
* **SoundEnd**

## Enumeration

`ResponseMode1`

## Fields

| Name |
|  --- |
| `NOTREQUIRED` |
| `IMMEDIATE` |
| `PRINTEND` |
| `SOUNDEND` |

## Example

```python
from adyen.models.response_mode_1 import ResponseMode1

response_mode_1 = ResponseMode1.PRINTEND
```

