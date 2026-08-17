
# Ultimate Parent Company Business Details 2

Details about the ultimate parent company's business.

## Structure

`UltimateParentCompanyBusinessDetails2`

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
from adyen.models.ultimate_parent_company_business_details_2 import UltimateParentCompanyBusinessDetails2

ultimate_parent_company_business_details_2 = UltimateParentCompanyBusinessDetails2(
    legal_business_name='legalBusinessName8',
    registration_number='registrationNumber6',
    stock_exchange='stockExchange4',
    stock_number='stockNumber6',
    stock_ticker='stockTicker6'
)
```

