
# Channel 2 Enum

The platform where a payment transaction takes place. This field is optional for filtering out payment methods that are only available on specific platforms. If this value is not set, then we will try to infer it from the `sdkVersion` or `token`.

Possible values:

* iOS
* Android
* Web

## Enumeration

`Channel2Enum`

## Fields

| Name |
|  --- |
| `IOS` |
| `ANDROID` |
| `WEB` |

## Example

```python
from adyen.models.channel_2_enum import Channel2Enum

channel_2 = Channel2Enum.IOS
```

