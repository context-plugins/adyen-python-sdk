
# Forex Quote 2

The forex quote as returned in the response of the forex service.

*This model accepts additional fields of type Any.*

## Structure

`ForexQuote2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account` | `str` | Optional | The account name. |
| `account_type` | `str` | Optional | The account type. |
| `base_amount` | [`BaseAmount`](../../doc/models/base-amount.md) | Optional | - |
| `base_points` | `int` | Required | The base points. |
| `buy` | [`Buy`](../../doc/models/buy.md) | Optional | - |
| `interbank` | [`Interbank`](../../doc/models/interbank.md) | Optional | - |
| `reference` | `str` | Optional | The reference assigned to the forex quote request. |
| `sell` | [`Sell`](../../doc/models/sell.md) | Optional | - |
| `signature` | `str` | Optional | The signature to validate the integrity. |
| `source` | `str` | Optional | The source of the forex quote. |
| `mtype` | `str` | Optional | The type of forex. |
| `valid_till` | `datetime` | Required | The date until which the forex quote is valid. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from adyen.models.base_amount import BaseAmount
from adyen.models.buy import Buy
from adyen.models.forex_quote_2 import ForexQuote2
from adyen.models.interbank import Interbank

forex_quote_2 = ForexQuote2(
    base_points=130,
    valid_till=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    account='account6',
    account_type='accountType6',
    base_amount=BaseAmount(
        currency='currency8',
        value=202,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    buy=Buy(
        currency='currency2',
        value=72,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    interbank=Interbank(
        currency='currency4',
        value=244,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

