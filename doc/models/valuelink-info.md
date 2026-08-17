
# Valuelink Info

## Structure

`ValuelinkInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `authorisation_mid` | `str` | Required | Authorisation Mid |
| `pin_support` | [`PinSupportEnum`](../../doc/models/pin-support-enum.md) | Required | PIN Support. For ecommerce, PIN is required. |
| `submitter_id` | `str` | Optional | Submitter ID |
| `terminal_id` | `str` | Optional | Terminal ID |

## Example

```python
from adyen.models.pin_support_enum import PinSupportEnum
from adyen.models.valuelink_info import ValuelinkInfo

valuelink_info = ValuelinkInfo(
    authorisation_mid='authorisationMid2',
    pin_support=PinSupportEnum.PIN,
    submitter_id='submitterId8',
    terminal_id='terminalId4'
)
```

