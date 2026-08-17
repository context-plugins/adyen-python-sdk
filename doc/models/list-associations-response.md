
# List Associations Response

## Structure

`ListAssociationsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `links` | [`Link3`](../../doc/models/link-3.md) | Required | A list of hyperlinks to resources related to this response. |
| `data` | [`List[AssociationListing]`](../../doc/models/association-listing.md) | Required | Contains a list of associations and their corresponding details. |
| `items_total` | `int` | Required | The total number of items available. |
| `pages_total` | `int` | Required | The total number of pages available. |

## Example

```python
import dateutil.parser

from adyen.models.association_listing import AssociationListing
from adyen.models.association_status_1_enum import AssociationStatus1Enum
from adyen.models.link_3 import Link3
from adyen.models.links_element import LinksElement
from adyen.models.list_associations_response import ListAssociationsResponse
from adyen.models.sca_device_type_3_enum import ScaDeviceType3Enum
from adyen.models.sca_entity_type_2_enum import ScaEntityType2Enum

list_associations_response = ListAssociationsResponse(
    links=Link3(
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
    data=[
        AssociationListing(
            created_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
            entity_id='entityId8',
            entity_type=ScaEntityType2Enum.LEGALENTITY,
            sca_device_id='BSDR11111111111A1AAA1AAAAA1AA1',
            sca_device_type=ScaDeviceType3Enum.ANDROID,
            status=AssociationStatus1Enum.PENDINGAPPROVAL,
            sca_device_name='scaDeviceName0'
        )
    ],
    items_total=1,
    pages_total=1
)
```

