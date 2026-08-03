
# Search Registered Devices Response

*This model accepts additional fields of type Any.*

## Structure

`SearchRegisteredDevicesResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `data` | [`List[Device]`](../../doc/models/device.md) | Optional | Contains a list of registered SCA devices and their corresponding details. |
| `items_total` | `int` | Optional | The total amount of registered SCA devices that match the query parameters. |
| `link` | [`Link`](../../doc/models/link.md) | Optional | - |
| `pages_total` | `int` | Optional | The total amount of list pages. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.device import Device
from adyen.models.first import First
from adyen.models.last import Last
from adyen.models.link import Link
from adyen.models.mself import Self
from adyen.models.next import Next
from adyen.models.previous import Previous
from adyen.models.search_registered_devices_response import SearchRegisteredDevicesResponse
from adyen.models.type_10 import Type10

search_registered_devices_response = SearchRegisteredDevicesResponse(
    data=[
        Device(
            id='id0',
            name='name0',
            payment_instrument_id='paymentInstrumentId2',
            mtype=Type10.BROWSER,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        Device(
            id='id0',
            name='name0',
            payment_instrument_id='paymentInstrumentId2',
            mtype=Type10.BROWSER,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    items_total=246,
    link=Link(
        first=First(
            href='href2',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        last=Last(
            href='href2',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        next=Next(
            href='href4',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        previous=Previous(
            href='href0',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        mself=Self(
            href='href0',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    pages_total=208,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

