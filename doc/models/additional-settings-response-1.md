
# Additional Settings Response 1

Additional shopper and transaction information to be included in your [standard webhooks](https://docs.adyen.com/development-resources/webhooks/webhook-types/#event-codes). Find out more about the available [additional settings](https://docs.adyen.com/development-resources/webhooks/additional-settings).

*This model accepts additional fields of type Any.*

## Structure

`AdditionalSettingsResponse1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `exclude_event_codes` | `List[str]` | Optional | Object containing list of event codes for which the notification will not be sent. |
| `include_event_codes` | `List[str]` | Optional | Object containing list of event codes for which the notification will be sent. |
| `properties` | `Dict[str, bool]` | Optional | Object containing boolean key-value pairs. The key can be any [standard webhook additional setting](https://docs.adyen.com/development-resources/webhooks/additional-settings), and the value indicates if the setting is enabled.<br>For example, `includeCaptureDelayHours`: **true** means the standard notifications you get will contain the number of hours remaining until the payment will be captured. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.additional_settings_response_1 import AdditionalSettingsResponse1

additional_settings_response_1 = AdditionalSettingsResponse1(
    exclude_event_codes=[
        'excludeEventCodes8',
        'excludeEventCodes9',
        'excludeEventCodes0'
    ],
    include_event_codes=[
        'includeEventCodes6',
        'includeEventCodes7',
        'includeEventCodes8'
    ],
    properties={
        'key0': False
    },
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

