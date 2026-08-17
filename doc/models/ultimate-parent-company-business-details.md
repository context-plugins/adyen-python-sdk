
# Ultimate Parent Company Business Details

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

## Example

```python
from adyen.models.ultimate_parent_company_business_details import UltimateParentCompanyBusinessDetails

ultimate_parent_company_business_details = UltimateParentCompanyBusinessDetails(
    legal_business_name='legalBusinessName4',
    registration_number='registrationNumber8',
    stock_exchange='stockExchange0',
    stock_number='stockNumber8',
    stock_ticker='stockTicker2'
)
```

