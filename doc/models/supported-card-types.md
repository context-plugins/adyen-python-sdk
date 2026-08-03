
# Supported Card Types

*This model accepts additional fields of type Any.*

## Structure

`SupportedCardTypes`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `credit` | `bool` | Optional | Set to **true** to accept credit cards. |
| `debit` | `bool` | Optional | Set to **true** to accept debit cards. |
| `deferred_debit` | `bool` | Optional | Set to **true** to accept cards that allow deferred debit. |
| `prepaid` | `bool` | Optional | Set to **true** to accept prepaid cards. |
| `unknown` | `bool` | Optional | Set to **true** to accept card types for which the terminal can't determine the funding source while offline. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.supported_card_types import SupportedCardTypes

supported_card_types = SupportedCardTypes(
    credit=False,
    debit=False,
    deferred_debit=False,
    prepaid=False,
    unknown=False,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

