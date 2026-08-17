
# Response Mode 1 Enum

Message response awaited by the initiator of the Request. Allows various types and synchronisation of requests for Print or Sound.
Possible values:

* **Immediate**
* **NotRequired**
* **PrintEnd**
* **SoundEnd**

## Enumeration

`ResponseMode1Enum`

## Fields

| Name |
|  --- |
| `NOTREQUIRED` |
| `IMMEDIATE` |
| `PRINTEND` |
| `SOUNDEND` |

## Example

```python
from adyen.models.response_mode_1_enum import ResponseMode1Enum

response_mode_1 = ResponseMode1Enum.PRINTEND
```

