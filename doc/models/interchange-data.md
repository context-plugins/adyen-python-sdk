
# Interchange Data

*This model accepts additional fields of type Any.*

## Structure

`InterchangeData`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `interchange_amount` | [`InterchangeAmount`](../../doc/models/interchange-amount.md) | Optional | - |
| `interchange_rate_indicator` | `str` | Optional | A 3-character alphanumeric code assigned by Visa that identifies the specific interchange reimbursement program a transaction qualified for. The code is assigned based on the card type, entry mode, and security data provided. |
| `mtype` | [`Type85`](../../doc/models/type-85.md) | Required | The type of events data.<br><br>Possible values:<br><br>- **interchangeData**: information about the interchange fee applied to a transaction. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.interchange_amount import InterchangeAmount
from adyen.models.interchange_data import InterchangeData
from adyen.models.type_85 import Type85

interchange_data = InterchangeData(
    mtype=Type85.INTERCHANGEDATA,
    interchange_amount=InterchangeAmount(
        currency='currency2',
        value=62,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    interchange_rate_indicator='interchangeRateIndicator6',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

