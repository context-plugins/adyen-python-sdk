
# Search Registered Devices Response

## Structure

`SearchRegisteredDevicesResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `data` | [`List[Device]`](../../doc/models/device.md) | Optional | Contains a list of registered SCA devices and their corresponding details. |
| `items_total` | `int` | Optional | The total amount of registered SCA devices that match the query parameters. |
| `link` | [`Link1`](../../doc/models/link-1.md) | Optional | Contains links to the list pages. |
| `pages_total` | `int` | Optional | The total amount of list pages. |

## Example

```python
from adyen.models.device import Device
from adyen.models.link_1 import Link1
from adyen.models.links_element import LinksElement
from adyen.models.search_registered_devices_response import SearchRegisteredDevicesResponse
from adyen.models.type_101_enum import Type101Enum

search_registered_devices_response = SearchRegisteredDevicesResponse(
    data=[
        Device(
            id='id0',
            name='name0',
            payment_instrument_id='paymentInstrumentId2',
            mtype=Type101Enum.BROWSER
        ),
        Device(
            id='id0',
            name='name0',
            payment_instrument_id='paymentInstrumentId2',
            mtype=Type101Enum.BROWSER
        )
    ],
    items_total=246,
    link=Link1(
        first=LinksElement(
            href='href2'
        ),
        last=LinksElement(
            href='href2'
        ),
        next=LinksElement(
            href='href4'
        ),
        previous=LinksElement(
            href='href0'
        ),
        mself=LinksElement(
            href='href0'
        )
    ),
    pages_total=208
)
```

