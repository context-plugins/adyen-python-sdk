
# Href 3

A short-lived URL that redirects the user to the iDEAL profile management page.

## Structure

`Href3`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `href` | `str` | Required | The full URL for the redirection. |

## Example

```python
from adyen.models.href_3 import Href3

href_3 = Href3(
    href='https://someUrl'
)
```

