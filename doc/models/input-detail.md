
# Input Detail

*This model accepts additional fields of type Any.*

## Structure

`InputDetail`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `configuration` | `Dict[str, str]` | Optional | Configuration parameters for the required input. |
| `details` | [`List[SubInputDetail]`](../../doc/models/sub-input-detail.md) | Optional | Input details can also be provided recursively. |
| `input_details` | [`List[SubInputDetail]`](../../doc/models/sub-input-detail.md) | Optional | Input details can also be provided recursively (deprecated). |
| `item_search_url` | `str` | Optional | In case of a select, the URL from which to query the items. |
| `items` | [`List[NetworkTokenRequestor]`](../../doc/models/network-token-requestor.md) | Optional | In case of a select, the items to choose from. |
| `key` | `str` | Optional | The value to provide in the result. |
| `optional` | `bool` | Optional | True if this input value is optional. |
| `mtype` | `str` | Optional | The type of the required input. |
| `value` | `str` | Optional | The value can be pre-filled, if available. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.input_detail import InputDetail
from adyen.models.network_token_requestor import NetworkTokenRequestor
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
                NetworkTokenRequestor(
                    id='id8',
                    name='name8',
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                )
            ],
            key='key0',
            optional=False,
            mtype='type0',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        SubInputDetail(
            configuration={
                'key0': 'configuration6',
                'key1': 'configuration7'
            },
            items=[
                NetworkTokenRequestor(
                    id='id8',
                    name='name8',
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                )
            ],
            key='key0',
            optional=False,
            mtype='type0',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        SubInputDetail(
            configuration={
                'key0': 'configuration6',
                'key1': 'configuration7'
            },
            items=[
                NetworkTokenRequestor(
                    id='id8',
                    name='name8',
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                )
            ],
            key='key0',
            optional=False,
            mtype='type0',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    input_details=[
        SubInputDetail(
            configuration={
                'key0': 'configuration6'
            },
            items=[
                NetworkTokenRequestor(
                    id='id8',
                    name='name8',
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                ),
                NetworkTokenRequestor(
                    id='id8',
                    name='name8',
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                ),
                NetworkTokenRequestor(
                    id='id8',
                    name='name8',
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                )
            ],
            key='key0',
            optional=False,
            mtype='type0',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        SubInputDetail(
            configuration={
                'key0': 'configuration6'
            },
            items=[
                NetworkTokenRequestor(
                    id='id8',
                    name='name8',
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                ),
                NetworkTokenRequestor(
                    id='id8',
                    name='name8',
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                ),
                NetworkTokenRequestor(
                    id='id8',
                    name='name8',
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                )
            ],
            key='key0',
            optional=False,
            mtype='type0',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    item_search_url='itemSearchUrl6',
    items=[
        NetworkTokenRequestor(
            id='id8',
            name='name8',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        NetworkTokenRequestor(
            id='id8',
            name='name8',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

