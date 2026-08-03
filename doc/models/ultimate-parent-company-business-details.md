
# Ultimate Parent Company Business Details

*This model accepts additional fields of type Any.*

## Structure

`UltimateParentCompanyBusinessDetails`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `legal_business_name` | `str` | Optional | The legal name of the company. |
| `registration_number` | `str` | Optional | The registration number of the company. |
| `stock_exchange` | `str` | Optional | Market Identifier Code (MIC). |
| `stock_number` | `str` | Optional | International Securities Identification Number (ISIN). |
| `stock_ticker` | `str` | Optional | Stock Ticker symbol. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.ultimate_parent_company_business_details import UltimateParentCompanyBusinessDetails

ultimate_parent_company_business_details = UltimateParentCompanyBusinessDetails(
    legal_business_name='legalBusinessName4',
    registration_number='registrationNumber8',
    stock_exchange='stockExchange0',
    stock_number='stockNumber8',
    stock_ticker='stockTicker2',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

