
# Stock Data 2

Information about the organization's publicly traded stock. Provide this object only if `type` is **listedPublicCompany**.

*This model accepts additional fields of type Any.*

## Structure

`StockData2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `market_identifier` | `str` | Optional | The four-digit [Market Identifier Code](https://en.wikipedia.org/wiki/Market_Identifier_Code) of the stock market where the organization's stocks are traded. |
| `stock_number` | `str` | Optional | The 12-digit International Securities Identification Number (ISIN) of the company, without dashes (-). |
| `ticker_symbol` | `str` | Optional | The stock ticker symbol. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.stock_data_2 import StockData2

stock_data_2 = StockData2(
    market_identifier='marketIdentifier2',
    stock_number='stockNumber2',
    ticker_symbol='tickerSymbol8',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

