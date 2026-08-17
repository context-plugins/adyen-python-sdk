
# Valuelink Response Info

## Structure

`ValuelinkResponseInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `authorisation_mid` | `str` | Optional | Authorisation Mid |
| `pin_support` | [`PinSupportEnum`](../../doc/models/pin-support-enum.md) | Optional | PIN Support. For ecommerce, PIN is required. |
| `submitter_id` | `str` | Optional | Submitter ID |
| `terminal_id` | `str` | Optional | Terminal ID |

## Example

```python
from adyen.models.pin_support_enum import PinSupportEnum
from adyen.models.valuelink_response_info import ValuelinkResponseInfo

valuelink_response_info = ValuelinkResponseInfo(
    authorisation_mid='authorisationMid6',
    pin_support=PinSupportEnum.PIN,
    submitter_id='submitterId2',
    terminal_id='terminalId2'
)
```

