
# Links 21

Contains links to the next and previous page whenever applicable.

## Structure

`Links21`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `next` | [`LinksElement`](../../doc/models/links-element.md) | Optional | Contains a link to the next page. |
| `prev` | [`LinksElement`](../../doc/models/links-element.md) | Optional | Contains a link to the previous page. |

## Example

```python
from adyen.models.links_21 import Links21
from adyen.models.links_element import LinksElement

links_21 = Links21(
    next=LinksElement(
        href='href4'
    ),
    prev=LinksElement(
        href='href8'
    )
)
```

