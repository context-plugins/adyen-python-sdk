<!-- Generated file — do not edit; regenerated with the SDK. -->

# AccountCompanyLevel — operations

Accessor: `client.account_company_level` · Source: `adyen/apis/account_company_level.py` · 3 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.account_company_level.get_companies

- **Route**: `GET /companies`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default9`
- **Signature**: `def get_companies(*, page_number: int | None = None, page_size: int | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `page_number` — query `pageNumber` · `page_size` — query `pageSize`
- **Returns (parsed)**: `ListCompanyResponse`
- **Returns (raw)**: `ApiResult[ListCompanyResponse, GetCompaniesErrorBody]`
- **Error**: `GetCompaniesErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ListCompanyResponse` | `adyen/models/list_company_response.py` |
| `GetCompaniesErrorBody` | `adyen/errors/get_companies_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.account_company_level.get_companies_company_id

- **Route**: `GET /companies/{companyId}`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default9`
- **Signature**: `def get_companies_company_id(company_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `company_id`
- **Params**: `company_id` — path `companyId`
- **Returns (parsed)**: `Company2`
- **Returns (raw)**: `ApiResult[Company2, GetCompaniesCompanyIdErrorBody]`
- **Error**: `GetCompaniesCompanyIdErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `Company2` | `adyen/models/company2.py` |
| `GetCompaniesCompanyIdErrorBody` | `adyen/errors/get_companies_company_id_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.account_company_level.get_companies_company_id_merchants

- **Route**: `GET /companies/{companyId}/merchants`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default9`
- **Signature**: `def get_companies_company_id_merchants(company_id: str, *, page_number: int | None = None, page_size: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `company_id`
- **Params**: `company_id` — path `companyId` · `page_number` — query `pageNumber` · `page_size` — query `pageSize`
- **Returns (parsed)**: `ListMerchantResponse`
- **Returns (raw)**: `ApiResult[ListMerchantResponse, GetCompaniesCompanyIdMerchantsErrorBody]`
- **Error**: `GetCompaniesCompanyIdMerchantsErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ListMerchantResponse` | `adyen/models/list_merchant_response.py` |
| `GetCompaniesCompanyIdMerchantsErrorBody` | `adyen/errors/get_companies_company_id_merchants_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

