
# Expiry

## Structure

`Expiry`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `month` | `str` | Optional | The month in which the card will expire. |
| `year` | `str` | Optional | The year in which the card will expire. |

## Example

```python
from adyen.models.expiry import Expiry

expiry = Expiry(
    month='month8',
    year='year0'
)
```

