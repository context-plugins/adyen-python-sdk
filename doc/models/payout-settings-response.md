
# Payout Settings Response

*This model accepts additional fields of type Any.*

## Structure

`PayoutSettingsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `data` | [`List[PayoutSettings]`](../../doc/models/payout-settings.md) | Optional | The list of payout accounts. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.payout_settings import PayoutSettings
from adyen.models.payout_settings_response import PayoutSettingsResponse
from adyen.models.priority_1 import Priority1
from adyen.models.verification_status import VerificationStatus

payout_settings_response = PayoutSettingsResponse(
    data=[
        PayoutSettings(
            id='id0',
            transfer_instrument_id='transferInstrumentId8',
            allowed=False,
            enabled=False,
            enabled_from_date='enabledFromDate2',
            priority=Priority1.URGENT,
            verification_status=VerificationStatus.REJECTED,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        PayoutSettings(
            id='id0',
            transfer_instrument_id='transferInstrumentId8',
            allowed=False,
            enabled=False,
            enabled_from_date='enabledFromDate2',
            priority=Priority1.URGENT,
            verification_status=VerificationStatus.REJECTED,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        PayoutSettings(
            id='id0',
            transfer_instrument_id='transferInstrumentId8',
            allowed=False,
            enabled=False,
            enabled_from_date='enabledFromDate2',
            priority=Priority1.URGENT,
            verification_status=VerificationStatus.REJECTED,
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

