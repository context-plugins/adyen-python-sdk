
# Href 6

The URL to where the user must be redirected after a payment has been canceled.

## Structure

`Href6`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `href` | `str` | Required | The full URL for the redirection. |

## Example

```python
from adyen.models.href_6 import Href6

href_6 = Href6(
    href='https://someUrl'
)
```

