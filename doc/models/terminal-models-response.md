
# Terminal Models Response

## Structure

`TerminalModelsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `data` | [`List[Item]`](../../doc/models/item.md) | Optional | The terminal models that the API credential has access to. |

## Example

```python
from adyen.models.item import Item
from adyen.models.terminal_models_response import TerminalModelsResponse

terminal_models_response = TerminalModelsResponse(
    data=[
        Item(
            id='id0',
            name='name0'
        ),
        Item(
            id='id0',
            name='name0'
        )
    ]
)
```

