
# Expiry 2

The expiration date of the card.

## Structure

`Expiry2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `month` | `str` | Optional | The month in which the card will expire. |
| `year` | `str` | Optional | The year in which the card will expire. |

## Example

```python
from adyen.models.expiry_2 import Expiry2

expiry_2 = Expiry2(
    month='month0',
    year='year8'
)
```

