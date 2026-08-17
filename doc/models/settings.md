
# Settings

## Structure

`Settings`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `band` | `str` | Optional | The preferred Wi-Fi band, for use if the terminals support multiple bands. Possible values: All, 2.4GHz, 5GHz. |
| `roaming` | `bool` | Optional | Indicates whether roaming is enabled on the terminals. |
| `timeout` | `int` | Optional | The connection time-out in seconds. Minimum value: 0. |

## Example

```python
from adyen.models.settings import Settings

settings = Settings(
    band='band0',
    roaming=False,
    timeout=124
)
```

