
# Link 3

A list of hyperlinks to resources related to this response.

## Structure

`Link3`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `first` | [`LinksElement`](../../doc/models/links-element.md) | Optional | The link to the first page of the list. |
| `last` | [`LinksElement`](../../doc/models/links-element.md) | Optional | The link to the last page of the list. |
| `next` | [`LinksElement`](../../doc/models/links-element.md) | Optional | The link to the next page of the list. |
| `previous` | [`LinksElement`](../../doc/models/links-element.md) | Optional | The link to the previous page of the list. |
| `mself` | [`LinksElement`](../../doc/models/links-element.md) | Optional | The link to the list page you are currently viewing. |

## Example

```python
from adyen.models.link_3 import Link3
from adyen.models.links_element import LinksElement

link_3 = Link3(
    first=LinksElement(
        href='href2'
    ),
    last=LinksElement(
        href='href2'
    ),
    next=LinksElement(
        href='href4'
    ),
    previous=LinksElement(
        href='href0'
    ),
    mself=LinksElement(
        href='href0'
    )
)
```

