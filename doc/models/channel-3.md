
# Channel 3

The platform where a payment transaction takes place. This field can be used for filtering out payment methods that are only available on specific platforms. Possible values:

* iOS
* Android
* Web

## Enumeration

`Channel3`

## Fields

| Name |
|  --- |
| `IOS` |
| `ANDROID` |
| `WEB` |

## Example

```python
from adyen.models.channel_3 import Channel3

channel_3 = Channel3.ANDROID
```

