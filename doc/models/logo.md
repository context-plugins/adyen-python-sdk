
# Logo

## Structure

`Logo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `data` | `str` | Optional | The image file, converted to a Base64-encoded string, of the logo to be shown on the terminal.<br><br>**Constraints**: *Maximum Length*: `350000` |

## Example

```python
from adyen.models.logo import Logo

logo = Logo(
    data='data4'
)
```

