
# Supported Card Types 2

The type of card for which the terminal accepts store-and-forward payments. You can specify multiple card types.

*This model accepts additional fields of type Any.*

## Structure

`SupportedCardTypes2`

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

from adyen.models.supported_card_types_2 import SupportedCardTypes2

supported_card_types_2 = SupportedCardTypes2(
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

