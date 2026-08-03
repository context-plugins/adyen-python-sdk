
# Payout Settings

*This model accepts additional fields of type Any.*

## Structure

`PayoutSettings`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `allowed` | `bool` | Optional | Indicates if payouts to the bank account are allowed. This value is set automatically based on the status of the verification process. The value is:<br><br>* **true** if `verificationStatus` is **valid**.<br>* **false** for all other values. |
| `enabled` | `bool` | Optional | Indicates if payouts to this bank account are enabled. Default: **true**.<br><br>To receive payouts into this bank account, both `enabled` and `allowed` must be **true**. |
| `enabled_from_date` | `str` | Optional | The date when Adyen starts paying out to this bank account.<br><br>Format: [ISO 8601](https://www.w3.org/TR/NOTE-datetime), for example, **2019-11-23T12:25:28Z** or **2020-05-27T20:25:28+08:00**.<br><br>If not specified, the `enabled` field indicates if payouts are enabled for this bank account.<br><br>If a date is specified and:<br><br>* `enabled`: **true**, payouts are enabled starting the specified date.<br>* `enabled`: **false**, payouts are disabled until the specified date. On the specified date, `enabled` changes to **true** and this field is reset to **null**. |
| `id` | `str` | Required | The unique identifier of the payout setting. |
| `priority` | [`Priority1`](../../doc/models/priority-1.md) | Optional | - |
| `transfer_instrument_id` | `str` | Required | The unique identifier of the [transfer instrument](https://docs.adyen.com/api-explorer/#/legalentity/latest/post/transferInstruments) that contains the details of the bank account. |
| `verification_status` | [`VerificationStatus`](../../doc/models/verification-status.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.payout_settings import PayoutSettings
from adyen.models.priority_1 import Priority1
from adyen.models.verification_status import VerificationStatus

payout_settings = PayoutSettings(
    id='id4',
    transfer_instrument_id='transferInstrumentId8',
    allowed=False,
    enabled=False,
    enabled_from_date='enabledFromDate6',
    priority=Priority1.FIRST,
    verification_status=VerificationStatus.INVALID,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

