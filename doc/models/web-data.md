
# Web Data

## Structure

`WebData`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `web_address` | `str` | Optional | The URL of the website or the app store URL. |
| `web_address_id` | `str` | Optional, Read-only | The unique identifier of the web address. |

## Example

```python
from adyen.models.web_data import WebData

web_data = WebData(
    web_address='webAddress8'
)
```

