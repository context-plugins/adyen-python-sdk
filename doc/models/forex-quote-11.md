
# Forex Quote 11

The forex quote as returned in the response of the forex service.

## Structure

`ForexQuote11`

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
from adyen.models.forex_quote_11 import ForexQuote11

forex_quote_11 = ForexQuote11(
    base_points=234,
    valid_till=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    account='account0',
    account_type='accountType0',
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

