
# Url

## Structure

`Url`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `encrypted` | `bool` | Optional | Indicates if the message sent to this URL should be encrypted. |
| `password` | `str` | Optional | The password for authentication of the notifications. |
| `url` | `str` | Optional | The URL in the format: http(s)://domain.com. |
| `username` | `str` | Optional | The username for authentication of the notifications. |

## Example

```python
from adyen.models.url import Url

url = Url(
    encrypted=False,
    password='password8',
    url='url8',
    username='username6'
)
```

