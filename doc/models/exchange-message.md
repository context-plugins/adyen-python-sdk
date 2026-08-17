
# Exchange Message

## Structure

`ExchangeMessage`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `message_code` | `str` | Optional | - |
| `message_description` | `str` | Optional | - |

## Example

```python
from adyen.models.exchange_message import ExchangeMessage

exchange_message = ExchangeMessage(
    message_code='messageCode4',
    message_description='messageDescription2'
)
```

