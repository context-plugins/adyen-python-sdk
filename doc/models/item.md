
# Item

The token requestor is an entity who requested tokenization of the card for secure payments.

## Structure

`Item`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | The value to provide in the result. |
| `name` | `str` | Optional | The display name. |

## Example

```python
from adyen.models.item import Item

item = Item(
    id='id2',
    name='name2'
)
```

