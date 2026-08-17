
# Association Listing

## Structure

`AssociationListing`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `created_at` | `datetime` | Required | The date and time when the association was created. |
| `entity_id` | `str` | Required | The unique identifier of the entity.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `100` |
| `entity_type` | [`ScaEntityType2Enum`](../../doc/models/sca-entity-type-2-enum.md) | Required | The type of the entity.<br><br>Possible values: **accountHolder**, **legalEntity** or **paymentInstrument**. |
| `sca_device_id` | `str` | Required | The unique identifier of the SCA device.<br><br>**Constraints**: *Minimum Length*: `30`, *Maximum Length*: `30` |
| `sca_device_name` | `str` | Optional | The human-readable name for the SCA device that was registered.<br><br>**Constraints**: *Minimum Length*: `0`, *Maximum Length*: `64` |
| `sca_device_type` | [`ScaDeviceType3Enum`](../../doc/models/sca-device-type-3-enum.md) | Required | The type of the device. |
| `status` | [`AssociationStatus1Enum`](../../doc/models/association-status-1-enum.md) | Required | The status of the association.<br><br>Possible values: **active** or **pendingApproval**. |

## Example

```python
import dateutil.parser

from adyen.models.association_listing import AssociationListing
from adyen.models.association_status_1_enum import AssociationStatus1Enum
from adyen.models.sca_device_type_3_enum import ScaDeviceType3Enum
from adyen.models.sca_entity_type_2_enum import ScaEntityType2Enum

association_listing = AssociationListing(
    created_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    entity_id='entityId4',
    entity_type=ScaEntityType2Enum.ACCOUNTHOLDER,
    sca_device_id='BSDR11111111111A1AAA1AAAAA1AA1',
    sca_device_type=ScaDeviceType3Enum.IOS,
    status=AssociationStatus1Enum.PENDINGAPPROVAL,
    sca_device_name='scaDeviceName4'
)
```

