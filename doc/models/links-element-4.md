
# Links Element 4

Generates a new client key, used to authenticate client-side requests. When you generate a new one, the existing key remains valid for 24 hours.

## Structure

`LinksElement4`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `href` | `str` | Optional | - |

## Example

```python
from adyen.models.links_element_4 import LinksElement4

links_element_4 = LinksElement4(
    href='href8'
)
```

