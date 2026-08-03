
# Association Listing

*This model accepts additional fields of type Any.*

## Structure

`AssociationListing`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `created_at` | `datetime` | Required | The date and time when the association was created. |
| `entity_id` | `str` | Required | The unique identifier of the entity.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `100` |
| `entity_type` | [`ScaEntityType2`](../../doc/models/sca-entity-type-2.md) | Required | - |
| `sca_device_id` | `str` | Required | The unique identifier of the SCA device.<br><br>**Constraints**: *Minimum Length*: `30`, *Maximum Length*: `30` |
| `sca_device_name` | `str` | Optional | The human-readable name for the SCA device that was registered.<br><br>**Constraints**: *Minimum Length*: `0`, *Maximum Length*: `64` |
| `sca_device_type` | [`ScaDeviceType3`](../../doc/models/sca-device-type-3.md) | Required | - |
| `status` | [`AssociationStatus1`](../../doc/models/association-status-1.md) | Required | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from adyen.models.association_listing import AssociationListing
from adyen.models.association_status_1 import AssociationStatus1
from adyen.models.sca_device_type_3 import ScaDeviceType3
from adyen.models.sca_entity_type_2 import ScaEntityType2

association_listing = AssociationListing(
    created_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    entity_id='entityId4',
    entity_type=ScaEntityType2.ACCOUNTHOLDER,
    sca_device_id='BSDR11111111111A1AAA1AAAAA1AA1',
    sca_device_type=ScaDeviceType3.IOS,
    status=AssociationStatus1.PENDINGAPPROVAL,
    sca_device_name='scaDeviceName4',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

