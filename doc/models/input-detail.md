
# Input Detail

## Structure

`InputDetail`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `configuration` | `Dict[str, str]` | Optional | Configuration parameters for the required input. |
| `details` | [`List[SubInputDetail]`](../../doc/models/sub-input-detail.md) | Optional | Input details can also be provided recursively. |
| `input_details` | [`List[SubInputDetail]`](../../doc/models/sub-input-detail.md) | Optional | Input details can also be provided recursively (deprecated). |
| `item_search_url` | `str` | Optional | In case of a select, the URL from which to query the items. |
| `items` | [`List[Item]`](../../doc/models/item.md) | Optional | In case of a select, the items to choose from. |
| `key` | `str` | Optional | The value to provide in the result. |
| `optional` | `bool` | Optional | True if this input value is optional. |
| `mtype` | `str` | Optional | The type of the required input. |
| `value` | `str` | Optional | The value can be pre-filled, if available. |

## Example

```python
from adyen.models.input_detail import InputDetail
from adyen.models.item import Item
from adyen.models.sub_input_detail import SubInputDetail

input_detail = InputDetail(
    configuration={
        'key0': 'configuration2',
        'key1': 'configuration1'
    },
    details=[
        SubInputDetail(
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
        ),
        SubInputDetail(
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
        ),
        SubInputDetail(
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
    ],
    input_details=[
        SubInputDetail(
            configuration={
                'key0': 'configuration6'
            },
            items=[
                Item(
                    id='id8',
                    name='name8'
                ),
                Item(
                    id='id8',
                    name='name8'
                ),
                Item(
                    id='id8',
                    name='name8'
                )
            ],
            key='key0',
            optional=False,
            mtype='type0'
        ),
        SubInputDetail(
            configuration={
                'key0': 'configuration6'
            },
            items=[
                Item(
                    id='id8',
                    name='name8'
                ),
                Item(
                    id='id8',
                    name='name8'
                ),
                Item(
                    id='id8',
                    name='name8'
                )
            ],
            key='key0',
            optional=False,
            mtype='type0'
        )
    ],
    item_search_url='itemSearchUrl6',
    items=[
        Item(
            id='id8',
            name='name8'
        ),
        Item(
            id='id8',
            name='name8'
        )
    ]
)
```

