
# Recurring 2

The recurring settings for the payment. Use this property when you want to enable [recurring payments](https://docs.adyen.com/online-payments/tokenization).

*This model accepts additional fields of type Any.*

## Structure

`Recurring2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `contract` | [`Contract`](../../doc/models/contract.md) | Optional | - |
| `recurring_detail_name` | `str` | Optional | A descriptive name for this detail. |
| `recurring_expiry` | `datetime` | Optional | Date after which no further authorisations shall be performed. Only for 3D Secure 2. |
| `recurring_frequency` | `str` | Optional | Minimum number of days between authorisations. Only for 3D Secure 2. |
| `token_service` | [`TokenService`](../../doc/models/token-service.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from adyen.models.contract import Contract
from adyen.models.recurring_2 import Recurring2
from adyen.models.token_service import TokenService

recurring_2 = Recurring2(
    contract=Contract.RECURRING,
    recurring_detail_name='recurringDetailName2',
    recurring_expiry=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    recurring_frequency='recurringFrequency4',
    token_service=TokenService.VISATOKENSERVICE,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

