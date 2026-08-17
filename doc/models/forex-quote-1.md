
# Forex Quote 1

## Structure

`ForexQuote1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account` | `str` | Optional | The account name. |
| `account_type` | `str` | Optional | The account type. |
| `base_amount` | [`Amount`](../../doc/models/amount.md) | Optional | The base amount. |
| `base_points` | `int` | Required | The base points. |
| `buy` | [`Amount`](../../doc/models/amount.md) | Optional | The buy rate. |
| `interbank` | [`Amount`](../../doc/models/amount.md) | Optional | The interbank amount. |
| `reference` | `str` | Optional | The reference assigned to the forex quote request. |
| `sell` | [`Amount`](../../doc/models/amount.md) | Optional | The sell rate. |
| `signature` | `str` | Optional | The signature to validate the integrity. |
| `source` | `str` | Optional | The source of the forex quote. |
| `mtype` | `str` | Optional | The type of forex. |
| `valid_till` | `datetime` | Required | The date until which the forex quote is valid. |

## Example

```python
import dateutil.parser

from adyen.models.amount import Amount
from adyen.models.forex_quote_1 import ForexQuote1

forex_quote_1 = ForexQuote1(
    base_points=146,
    valid_till=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    account='account2',
    account_type='accountType2',
    base_amount=Amount(
        currency='currency8',
        value=202
    ),
    buy=Amount(
        currency='currency2',
        value=72
    ),
    interbank=Amount(
        currency='currency4',
        value=244
    )
)
```

