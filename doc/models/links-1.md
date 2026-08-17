
# Links 1

References to resources connected with this user.

## Structure

`Links1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mself` | [`LinksElement6`](../../doc/models/links-element-6.md) | Required | Link to the resource itself. |

## Example

```python
from adyen.models.links_1 import Links1
from adyen.models.links_element_6 import LinksElement6

links_1 = Links1(
    mself=LinksElement6(
        href='href0'
    )
)
```

