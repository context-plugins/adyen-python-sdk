
# Href 4

A short-lived URL that redirects the user to the iDEAL page that is required for authentication.

## Structure

`Href4`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `href` | `str` | Required | The full URL for the redirection. |

## Example

```python
from adyen.models.href_4 import Href4

href_4 = Href4(
    href='https://someUrl'
)
```

