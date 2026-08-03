
# Expiry 2

The expiration date of the card.

*This model accepts additional fields of type Any.*

## Structure

`Expiry2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `month` | `str` | Optional | The month in which the card will expire. |
| `year` | `str` | Optional | The year in which the card will expire. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.expiry_2 import Expiry2

expiry_2 = Expiry2(
    month='month0',
    year='year8',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

