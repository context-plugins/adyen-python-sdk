
# Links 2

References to resources linked to the allowed origin.

## Structure

`Links2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mself` | [`LinksElement6`](../../doc/models/links-element-6.md) | Required | Link to the resource itself. |

## Example

```python
from adyen.models.links_2 import Links2
from adyen.models.links_element_6 import LinksElement6

links_2 = Links2(
    mself=LinksElement6(
        href='href0'
    )
)
```

