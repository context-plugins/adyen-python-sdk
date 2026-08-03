
# Expiry

*This model accepts additional fields of type Any.*

## Structure

`Expiry`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `month` | `str` | Optional | The month in which the card will expire. |
| `year` | `str` | Optional | The year in which the card will expire. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.expiry import Expiry

expiry = Expiry(
    month='month8',
    year='year0',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

