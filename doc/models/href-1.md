
# Href 1

The URL to where the user must be redirected after a successful payment.

## Structure

`Href1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `href` | `str` | Required | The full URL for the redirection. |

## Example

```python
from adyen.models.href_1 import Href1

href_1 = Href1(
    href='https://someUrl'
)
```

