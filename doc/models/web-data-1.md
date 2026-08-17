
# Web Data 1

The website and app URL of the legal entity.

## Structure

`WebData1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `web_address` | `str` | Optional | The URL of the website or the app store URL. |
| `web_address_id` | `str` | Optional, Read-only | The unique identifier of the web address. |

## Example

```python
from adyen.models.web_data_1 import WebData1

web_data_1 = WebData1(
    web_address='webAddress4'
)
```

