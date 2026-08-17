
# Links 7

Reference to resources connected with the store.

## Structure

`Links7`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mself` | [`LinksElement6`](../../doc/models/links-element-6.md) | Required | Link to the resource itself. |

## Example

```python
from adyen.models.links_7 import Links7
from adyen.models.links_element_6 import LinksElement6

links_7 = Links7(
    mself=LinksElement6(
        href='href0'
    )
)
```

