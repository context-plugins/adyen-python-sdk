
# Standalone 1

Settings for [standalone](https://docs.adyen.com/point-of-sale/standalone/standalone-build/set-up-standalone#set-up-standalone-using-an-api-call) features.

*This model accepts additional fields of type Any.*

## Structure

`Standalone1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `currency_code` | `str` | Optional | The default currency of the standalone payment terminal as an [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) currency code.<br><br>**Constraints**: *Minimum Length*: `3`, *Maximum Length*: `3` |
| `enable_gratuities` | `bool` | Optional | Indicates whether the tipping options specified in `gratuities` are enabled on the standalone terminal. |
| `enable_standalone` | `bool` | Optional | Enable standalone mode. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.standalone_1 import Standalone1

standalone_1 = Standalone1(
    currency_code='currencyCode4',
    enable_gratuities=False,
    enable_standalone=False,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

