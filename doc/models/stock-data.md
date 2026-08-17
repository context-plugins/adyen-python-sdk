
# Stock Data

## Structure

`StockData`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `market_identifier` | `str` | Optional | The four-digit [Market Identifier Code](https://en.wikipedia.org/wiki/Market_Identifier_Code) of the stock market where the organization's stocks are traded. |
| `stock_number` | `str` | Optional | The 12-digit International Securities Identification Number (ISIN) of the company, without dashes (-). |
| `ticker_symbol` | `str` | Optional | The stock ticker symbol. |

## Example

```python
from adyen.models.stock_data import StockData

stock_data = StockData(
    market_identifier='marketIdentifier4',
    stock_number='stockNumber0',
    ticker_symbol='tickerSymbol0'
)
```

