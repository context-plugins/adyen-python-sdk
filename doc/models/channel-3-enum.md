
# Channel 3 Enum

The platform where a payment transaction takes place. This field can be used for filtering out payment methods that are only available on specific platforms. Possible values:

* iOS
* Android
* Web

## Enumeration

`Channel3Enum`

## Fields

| Name |
|  --- |
| `IOS` |
| `ANDROID` |
| `WEB` |

## Example

```python
from adyen.models.channel_3_enum import Channel3Enum

channel_3 = Channel3Enum.ANDROID
```

