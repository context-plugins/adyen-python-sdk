
# Financier

*This model accepts additional fields of type Any.*

## Structure

`Financier`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amount` | [`Amount64`](../../doc/models/amount-64.md) | Required | - |
| `first_name` | `str` | Required | The financier's first name. |
| `last_name` | `str` | Required | The financier's last name. |
| `location` | `str` | Required | The city and country/region where the financier is currently located. For example: Chicago, USA |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.amount_64 import Amount64
from adyen.models.financier import Financier

financier = Financier(
    amount=Amount64(
        currency='currency2',
        value=110,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    first_name='firstName0',
    last_name='lastName8',
    location='location8',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

