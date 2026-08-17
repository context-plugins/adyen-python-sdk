
# Provider

## Structure

`Provider`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `logo_url` | `str` | Required | The URL of the organization's or brand's logo. This URL typically points to an image file (e.g., .png, .jpg, .svg) that can be displayed to visually represent the entity.<br><br>**Constraints**: *Minimum Length*: `1` |
| `name` | `str` | Required | The official or commonly used name of the organization, brand, or entity.<br><br>**Constraints**: *Minimum Length*: `1` |

## Example

```python
from adyen.models.provider import Provider

provider = Provider(
    logo_url='logoURL6',
    name='name8'
)
```

