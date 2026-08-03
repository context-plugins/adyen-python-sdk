
# Browser Info 2

*This model accepts additional fields of type Any.*

## Structure

`BrowserInfo2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `accept_header` | `str` | Required | The accept header value of the shopper's browser. |
| `color_depth` | `int` | Required | The color depth of the shopper's browser in bits per pixel. This should be obtained by using the browser's `screen.colorDepth` property. Accepted values: 1, 4, 8, 15, 16, 24, 30, 32 or 48 bit color depth. |
| `java_enabled` | `bool` | Required | Boolean value indicating if the shopper's browser is able to execute Java. |
| `java_script_enabled` | `bool` | Optional | Boolean value indicating if the shopper's browser is able to execute JavaScript. A default 'true' value is assumed if the field is not present.<br><br>**Default**: `True` |
| `language` | `str` | Required | The `navigator.language` value of the shopper's browser (as defined in IETF BCP 47). |
| `screen_height` | `int` | Required | The total height of the shopper's device screen in pixels. |
| `screen_width` | `int` | Required | The total width of the shopper's device screen in pixels. |
| `time_zone_offset` | `int` | Required | Time difference between UTC time and the shopper's browser local time, in minutes. |
| `user_agent` | `str` | Required | The user agent value of the shopper's browser. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.browser_info_2 import BrowserInfo2

browser_info_2 = BrowserInfo2(
    accept_header='acceptHeader8',
    color_depth=124,
    java_enabled=False,
    language='language2',
    screen_height=150,
    screen_width=130,
    time_zone_offset=182,
    user_agent='userAgent6',
    java_script_enabled=True,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

