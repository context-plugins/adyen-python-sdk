
# Additional Settings 1

Additional shopper and transaction information to be included in your [standard webhooks](https://docs.adyen.com/development-resources/webhooks/webhook-types/#event-codes). Find out more about the available [additional settings](https://docs.adyen.com/development-resources/webhooks/additional-settings).

## Structure

`AdditionalSettings1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `include_event_codes` | `List[str]` | Optional | Object containing list of event codes for which the notification will be sent. |
| `properties` | `Dict[str, bool]` | Optional | Object containing boolean key-value pairs. The key can be any [standard webhook additional setting](https://docs.adyen.com/development-resources/webhooks/additional-settings), and the value indicates if the setting is enabled.<br>For example, `includeCaptureDelayHours`: **true** means the standard notifications you get will contain the number of hours remaining until the payment will be captured. |

## Example

```python
from adyen.models.additional_settings_1 import AdditionalSettings1

additional_settings_1 = AdditionalSettings1(
    include_event_codes=[
        'includeEventCodes2',
        'includeEventCodes3',
        'includeEventCodes4'
    ],
    properties={
        'key0': False
    }
)
```

