
# Exchange Message

*This model accepts additional fields of type Any.*

## Structure

`ExchangeMessage`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `message_code` | `str` | Optional | - |
| `message_description` | `str` | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.exchange_message import ExchangeMessage

exchange_message = ExchangeMessage(
    message_code='messageCode4',
    message_description='messageDescription2',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

