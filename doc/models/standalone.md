
# Standalone

*This model accepts additional fields of type Any.*

## Structure

`Standalone`

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

from adyen.models.standalone import Standalone

standalone = Standalone(
    currency_code='currencyCode2',
    enable_gratuities=False,
    enable_standalone=False,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

