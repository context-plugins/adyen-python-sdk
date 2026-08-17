
# Sub Input Detail

## Structure

`SubInputDetail`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `configuration` | `Dict[str, str]` | Optional | Configuration parameters for the required input. |
| `items` | [`List[Item]`](../../doc/models/item.md) | Optional | In case of a select, the items to choose from. |
| `key` | `str` | Optional | The value to provide in the result. |
| `optional` | `bool` | Optional | True if this input is optional to provide. |
| `mtype` | `str` | Optional | The type of the required input. |
| `value` | `str` | Optional | The value can be pre-filled, if available. |

## Example

```python
from adyen.models.item import Item
from adyen.models.sub_input_detail import SubInputDetail

sub_input_detail = SubInputDetail(
    configuration={
        'key0': 'configuration6',
        'key1': 'configuration7'
    },
    items=[
        Item(
            id='id8',
            name='name8'
        )
    ],
    key='key0',
    optional=False,
    mtype='type0'
)
```

