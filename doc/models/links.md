
# Links

## Structure

`Links`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mself` | [`LinksElement6`](../../doc/models/links-element-6.md) | Required | Link to the resource itself. |

## Example

```python
from adyen.models.links import Links
from adyen.models.links_element_6 import LinksElement6

links = Links(
    mself=LinksElement6(
        href='href0'
    )
)
```

