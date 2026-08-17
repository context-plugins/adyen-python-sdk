
# Financial Report

## Structure

`FinancialReport`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `annual_turnover` | `str` | Optional | The annual turnover of the business. |
| `balance_sheet_total` | `str` | Optional | The balance sheet total of the business. |
| `currency_of_financial_data` | `str` | Optional | The currency used for the annual turnover, balance sheet total, and net assets. |
| `date_of_financial_data` | `str` | Optional | The date the financial data were provided, in YYYY-MM-DD format. |
| `employee_count` | `str` | Optional | The number of employees of the business. |
| `net_assets` | `str` | Optional | The net assets of the business. |

## Example

```python
from adyen.models.financial_report import FinancialReport

financial_report = FinancialReport(
    annual_turnover='annualTurnover8',
    balance_sheet_total='balanceSheetTotal6',
    currency_of_financial_data='currencyOfFinancialData8',
    date_of_financial_data='dateOfFinancialData2',
    employee_count='employeeCount2'
)
```

