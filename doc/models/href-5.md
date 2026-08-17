
# Href 5

A short-lived URL that redirects the user to the iDEAL profile registration page.

## Structure

`Href5`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `href` | `str` | Required | The full URL for the redirection. |

## Example

```python
from adyen.models.href_5 import Href5

href_5 = Href5(
    href='https://someUrl'
)
```

