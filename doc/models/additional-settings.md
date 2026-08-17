
# Additional Settings

## Structure

`AdditionalSettings`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `include_event_codes` | `List[str]` | Optional | Object containing list of event codes for which the notification will be sent. |
| `properties` | `Dict[str, bool]` | Optional | Object containing boolean key-value pairs. The key can be any [standard webhook additional setting](https://docs.adyen.com/development-resources/webhooks/additional-settings), and the value indicates if the setting is enabled.<br>For example, `includeCaptureDelayHours`: **true** means the standard notifications you get will contain the number of hours remaining until the payment will be captured. |

## Example

```python
from adyen.models.additional_settings import AdditionalSettings

additional_settings = AdditionalSettings(
    include_event_codes=[
        'includeEventCodes0',
        'includeEventCodes1',
        'includeEventCodes2'
    ],
    properties={
        'key0': False
    }
)
```

