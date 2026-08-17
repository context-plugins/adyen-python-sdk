
# Pagination Links 1

Pagination references.

## Structure

`PaginationLinks1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `first` | [`LinksElement9`](../../doc/models/links-element-9.md) | Required | The first page. |
| `last` | [`LinksElement10`](../../doc/models/links-element-10.md) | Required | The last page. |
| `next` | [`LinksElement11`](../../doc/models/links-element-11.md) | Optional | The next page. Only present if there is a next page. |
| `prev` | [`LinksElement12`](../../doc/models/links-element-12.md) | Optional | The previous page. Only present if there is a previous page. |
| `mself` | [`LinksElement13`](../../doc/models/links-element-13.md) | Required | The current page. |

## Example

```python
from adyen.models.links_element_10 import LinksElement10
from adyen.models.links_element_11 import LinksElement11
from adyen.models.links_element_12 import LinksElement12
from adyen.models.links_element_13 import LinksElement13
from adyen.models.links_element_9 import LinksElement9
from adyen.models.pagination_links_1 import PaginationLinks1

pagination_links_1 = PaginationLinks1(
    first=LinksElement9(
        href='href2'
    ),
    last=LinksElement10(
        href='href2'
    ),
    mself=LinksElement13(
        href='href0'
    ),
    next=LinksElement11(
        href='href4'
    ),
    prev=LinksElement12(
        href='href8'
    )
)
```

