
# List Associations Response

*This model accepts additional fields of type Any.*

## Structure

`ListAssociationsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `links` | [`Link`](../../doc/models/link.md) | Required | - |
| `data` | [`List[AssociationListing]`](../../doc/models/association-listing.md) | Required | Contains a list of associations and their corresponding details. |
| `items_total` | `int` | Required | The total number of items available. |
| `pages_total` | `int` | Required | The total number of pages available. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from adyen.models.association_listing import AssociationListing
from adyen.models.association_status_1 import AssociationStatus1
from adyen.models.first import First
from adyen.models.last import Last
from adyen.models.link import Link
from adyen.models.list_associations_response import ListAssociationsResponse
from adyen.models.mself import Self
from adyen.models.next import Next
from adyen.models.previous import Previous
from adyen.models.sca_device_type_3 import ScaDeviceType3
from adyen.models.sca_entity_type_2 import ScaEntityType2

list_associations_response = ListAssociationsResponse(
    links=Link(
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
    data=[
        AssociationListing(
            created_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
            entity_id='entityId8',
            entity_type=ScaEntityType2.LEGALENTITY,
            sca_device_id='BSDR11111111111A1AAA1AAAAA1AA1',
            sca_device_type=ScaDeviceType3.ANDROID,
            status=AssociationStatus1.PENDINGAPPROVAL,
            sca_device_name='scaDeviceName0',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    items_total=1,
    pages_total=1,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

