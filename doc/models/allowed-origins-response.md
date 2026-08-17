
# Allowed Origins Response

## Structure

`AllowedOriginsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `data` | [`List[AllowedOrigin]`](../../doc/models/allowed-origin.md) | Optional | List of allowed origins. |

## Example

```python
from adyen.models.allowed_origin import AllowedOrigin
from adyen.models.allowed_origins_response import AllowedOriginsResponse
from adyen.models.links_2 import Links2
from adyen.models.links_element_6 import LinksElement6

allowed_origins_response = AllowedOriginsResponse(
    data=[
        AllowedOrigin(
            domain='domain6',
            links=Links2(
                mself=LinksElement6(
                    href='href0'
                )
            ),
            id='id0'
        )
    ]
)
```

