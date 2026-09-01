<!-- Generated file — do not edit; regenerated with the SDK. -->

# UsersCompanyLevel — operations

Accessor: `client.users_company_level` · Source: `adyen/apis/users_company_level.py` · 4 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.users_company_level.get_companies_company_id_users

- **Route**: `GET /companies/{companyId}/users`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default9`
- **Signature**: `def get_companies_company_id_users(company_id: str, *, page_number: int | None = None, page_size: int | None = None, username: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `company_id`
- **Params**: `company_id` — path `companyId` · `page_number` — query `pageNumber` · `page_size` — query `pageSize` · `username` — query
- **Returns (parsed)**: `ListCompanyUsersResponse`
- **Returns (raw)**: `ApiResult[ListCompanyUsersResponse, GetCompaniesCompanyIdUsersErrorBody]`
- **Error**: `GetCompaniesCompanyIdUsersErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ListCompanyUsersResponse` | `adyen/models/list_company_users_response.py` |
| `GetCompaniesCompanyIdUsersErrorBody` | `adyen/errors/get_companies_company_id_users_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.users_company_level.get_companies_company_id_users_user_id

- **Route**: `GET /companies/{companyId}/users/{userId}`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default9`
- **Signature**: `def get_companies_company_id_users_user_id(company_id: str, user_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `company_id`, `user_id`
- **Params**: `company_id` — path `companyId` · `user_id` — path `userId`
- **Returns (parsed)**: `CompanyUser`
- **Returns (raw)**: `ApiResult[CompanyUser, GetCompaniesCompanyIdUsersUserIdErrorBody]`
- **Error**: `GetCompaniesCompanyIdUsersUserIdErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CompanyUser` | `adyen/models/company_user.py` |
| `GetCompaniesCompanyIdUsersUserIdErrorBody` | `adyen/errors/get_companies_company_id_users_user_id_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.users_company_level.patch_companies_company_id_users_user_id

- **Route**: `PATCH /companies/{companyId}/users/{userId}`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default9`
- **Signature**: `def patch_companies_company_id_users_user_id(company_id: str, user_id: str, *, body: UpdateCompanyUserRequest | UpdateCompanyUserRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `company_id`, `user_id`
- **Params**: `company_id` — path `companyId` · `user_id` — path `userId` · `body` — JSON body
- **Returns (parsed)**: `CompanyUser`
- **Returns (raw)**: `ApiResult[CompanyUser, PatchCompaniesCompanyIdUsersUserIdErrorBody]`
- **Error**: `PatchCompaniesCompanyIdUsersUserIdErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `UpdateCompanyUserRequest` | `adyen/models/update_company_user_request.py` |
| `UpdateCompanyUserRequestDict` | `adyen/models/update_company_user_request.py` |
| `CompanyUser` | `adyen/models/company_user.py` |
| `PatchCompaniesCompanyIdUsersUserIdErrorBody` | `adyen/errors/patch_companies_company_id_users_user_id_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.users_company_level.post_companies_company_id_users

- **Route**: `POST /companies/{companyId}/users`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default9`
- **Signature**: `def post_companies_company_id_users(company_id: str, *, body: CreateCompanyUserRequest | CreateCompanyUserRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `company_id`
- **Params**: `company_id` — path `companyId` · `body` — JSON body
- **Returns (parsed)**: `CreateCompanyUserResponse`
- **Returns (raw)**: `ApiResult[CreateCompanyUserResponse, PostCompaniesCompanyIdUsersErrorBody]`
- **Error**: `PostCompaniesCompanyIdUsersErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CreateCompanyUserRequest` | `adyen/models/create_company_user_request.py` |
| `CreateCompanyUserRequestDict` | `adyen/models/create_company_user_request.py` |
| `CreateCompanyUserResponse` | `adyen/models/create_company_user_response.py` |
| `PostCompaniesCompanyIdUsersErrorBody` | `adyen/errors/post_companies_company_id_users_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

