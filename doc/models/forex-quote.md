
# Forex Quote

## Structure

`ForexQuote`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account` | `str` | Optional | The account name. |
| `account_type` | `str` | Optional | The account type. |
| `base_amount` | [`Amount3`](../../doc/models/amount-3.md) | Optional | The base amount. |
| `base_points` | `int` | Required | The base points. |
| `buy` | [`Amount4`](../../doc/models/amount-4.md) | Optional | The buy rate. |
| `interbank` | [`Amount5`](../../doc/models/amount-5.md) | Optional | The interbank amount. |
| `reference` | `str` | Optional | The reference assigned to the forex quote request. |
| `sell` | [`Amount6`](../../doc/models/amount-6.md) | Optional | The sell rate. |
| `signature` | `str` | Optional | The signature to validate the integrity. |
| `source` | `str` | Optional | The source of the forex quote. |
| `mtype` | `str` | Optional | The type of forex. |
| `valid_till` | `datetime` | Required | The date until which the forex quote is valid. |

## Example

```python
import dateutil.parser

from adyen.models.amount_3 import Amount3
from adyen.models.amount_4 import Amount4
from adyen.models.amount_5 import Amount5
from adyen.models.forex_quote import ForexQuote

forex_quote = ForexQuote(
    base_points=186,
    valid_till=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    account='account6',
    account_type='accountType6',
    base_amount=Amount3(
        currency='currency8',
        value=202
    ),
    buy=Amount4(
        currency='currency2',
        value=72
    ),
    interbank=Amount5(
        currency='currency4',
        value=244
    )
)
```

