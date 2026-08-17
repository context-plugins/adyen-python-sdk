
# Avs Address

## Structure

`AvsAddress`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `street_address` | `str` | Required | The street and house number of the address.<br><br>Example: 1 Infinite Loop, Cupertino. |
| `zip` | `str` | Optional | The zip or post code of the address.<br><br>Example: CA 95014 |

## Example

```python
from adyen.models.avs_address import AvsAddress

avs_address = AvsAddress(
    street_address='streetAddress0',
    zip='zip6'
)
```

