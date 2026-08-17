
# Allowed Origin

## Structure

`AllowedOrigin`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `links` | [`Links2`](../../doc/models/links-2.md) | Optional | References to resources linked to the allowed origin. |
| `domain` | `str` | Required | Domain of the allowed origin. |
| `id` | `str` | Optional | Unique identifier of the allowed origin. |

## Example

```python
from adyen.models.allowed_origin import AllowedOrigin
from adyen.models.links_2 import Links2
from adyen.models.links_element_6 import LinksElement6

allowed_origin = AllowedOrigin(
    domain='https://adyen.com',
    links=Links2(
        mself=LinksElement6(
            href='href0'
        )
    ),
    id='id4'
)
```

