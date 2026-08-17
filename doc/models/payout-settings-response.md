
# Payout Settings Response

## Structure

`PayoutSettingsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `data` | [`List[PayoutSettings]`](../../doc/models/payout-settings.md) | Optional | The list of payout accounts. |

## Example

```python
from adyen.models.payout_settings import PayoutSettings
from adyen.models.payout_settings_response import PayoutSettingsResponse
from adyen.models.priority_enum import PriorityEnum
from adyen.models.verification_status_1_enum import VerificationStatus1Enum

payout_settings_response = PayoutSettingsResponse(
    data=[
        PayoutSettings(
            id='id0',
            transfer_instrument_id='transferInstrumentId8',
            allowed=False,
            enabled=False,
            enabled_from_date='enabledFromDate2',
            priority=PriorityEnum.URGENT,
            verification_status=VerificationStatus1Enum.REJECTED
        ),
        PayoutSettings(
            id='id0',
            transfer_instrument_id='transferInstrumentId8',
            allowed=False,
            enabled=False,
            enabled_from_date='enabledFromDate2',
            priority=PriorityEnum.URGENT,
            verification_status=VerificationStatus1Enum.REJECTED
        ),
        PayoutSettings(
            id='id0',
            transfer_instrument_id='transferInstrumentId8',
            allowed=False,
            enabled=False,
            enabled_from_date='enabledFromDate2',
            priority=PriorityEnum.URGENT,
            verification_status=VerificationStatus1Enum.REJECTED
        )
    ]
)
```

