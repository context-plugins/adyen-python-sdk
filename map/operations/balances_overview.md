<!-- Generated file — do not edit; regenerated with the SDK. -->

# BalancesOverview — operations

Accessor: `client.balances_overview` · Source: `adyen/apis/balances_overview.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.balances_overview.get_balance_overview_companies_company_account_code_balances

- **Route**: `GET /balanceOverview/companies/{companyAccountCode}/balances`
- **Server**: `default11`
- **Signature**: `def get_balance_overview_companies_company_account_code_balances(company_account_code: str, currency: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `company_account_code`, `currency`
- **Params**: `company_account_code` — path `companyAccountCode` · `currency` — query
- **Returns (parsed)**: `CompanyBalances`
- **Returns (raw)**: `ApiResult[CompanyBalances, GetBalanceOverviewCompaniesCompanyAccountCodeBalancesErrorBody]`
- **Error**: `GetBalanceOverviewCompaniesCompanyAccountCodeBalancesErrorBody` — **Case A (typed)**
- **Error arms**: `DefaultErrorResponseEntity` [401, 403, 422] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CompanyBalances` | `adyen/models/company_balances.py` |
| `GetBalanceOverviewCompaniesCompanyAccountCodeBalancesErrorBody` | `adyen/errors/get_balance_overview_companies_company_account_code_balances_error.py` |
| `DefaultErrorResponseEntity` | `adyen/models/default_error_response_entity.py` |

### client.balances_overview.get_balance_overview_merchants_merchant_account_code_balances

- **Route**: `GET /balanceOverview/merchants/{merchantAccountCode}/balances`
- **Server**: `default11`
- **Signature**: `def get_balance_overview_merchants_merchant_account_code_balances(merchant_account_code: str, currency: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `merchant_account_code`, `currency`
- **Params**: `merchant_account_code` — path `merchantAccountCode` · `currency` — query
- **Returns (parsed)**: `MerchantBalance`
- **Returns (raw)**: `ApiResult[MerchantBalance, GetBalanceOverviewMerchantsMerchantAccountCodeBalancesErrorBody]`
- **Error**: `GetBalanceOverviewMerchantsMerchantAccountCodeBalancesErrorBody` — **Case A (typed)**
- **Error arms**: `DefaultErrorResponseEntity` [401, 403, 422] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `MerchantBalance` | `adyen/models/merchant_balance.py` |
| `GetBalanceOverviewMerchantsMerchantAccountCodeBalancesErrorBody` | `adyen/errors/get_balance_overview_merchants_merchant_account_code_balances_error.py` |
| `DefaultErrorResponseEntity` | `adyen/models/default_error_response_entity.py` |

