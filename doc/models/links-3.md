
# Links 3

## Structure

`Links3`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `next` | [`LinksElement`](../../doc/models/links-element.md) | Optional | Contains a link to the next page. |
| `prev` | [`LinksElement`](../../doc/models/links-element.md) | Optional | Contains a link to the previous page. |

## Example

```python
from adyen.models.links_3 import Links3
from adyen.models.links_element import LinksElement

links_3 = Links3(
    next=LinksElement(
        href='href4'
    ),
    prev=LinksElement(
        href='href8'
    )
)
```

