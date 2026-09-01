<!-- Generated file — do not edit; regenerated with the SDK. -->

# DonationCampaigns — operations

Accessor: `client.donation_campaigns` · Source: `adyen/apis/donation_campaigns.py` · 6 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.donation_campaigns.delete_companies_company_id_campaign_management_donation_campaign_id

- **Route**: `DELETE /companies/{companyId}/campaignManagement/{donationCampaignId}`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default9`
- **Signature**: `def delete_companies_company_id_campaign_management_donation_campaign_id(company_id: str, donation_campaign_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `company_id`, `donation_campaign_id`
- **Params**: `company_id` — path `companyId` · `donation_campaign_id` — path `donationCampaignId`
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, DeleteCompaniesCompanyIdCampaignManagementDonationCampaignIdErrorBody]`
- **Error**: `DeleteCompaniesCompanyIdCampaignManagementDonationCampaignIdErrorBody` — **Case A (typed)**
- **Error arms**: `DefaultErrorResponseEntity` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DeleteCompaniesCompanyIdCampaignManagementDonationCampaignIdErrorBody` | `adyen/errors/delete_companies_company_id_campaign_management_donation_campaign_id_error.py` |
| `DefaultErrorResponseEntity` | `adyen/models/default_error_response_entity.py` |

### client.donation_campaigns.get_companies_company_id_campaign_management_account_holders_account_holder_id

- **Route**: `GET /companies/{companyId}/campaignManagement/accountHolders/{accountHolderId}`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default9`
- **Signature**: `def get_companies_company_id_campaign_management_account_holders_account_holder_id(company_id: str, account_holder_id: str, *, status: str | None = None, page_number: int | None = 1, page_size: int | None = 10, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `company_id`, `account_holder_id`
- **Params**: `company_id` — path `companyId` · `account_holder_id` — path `accountHolderId` · `status` — query · `page_number` — query `pageNumber` · `page_size` — query `pageSize`
- **Returns (parsed)**: `ListDonationCampaignsResponse`
- **Returns (raw)**: `ApiResult[ListDonationCampaignsResponse, GetCompaniesCompanyIdCampaignManagementAccountHoldersAccountHolderIdErrorBody]`
- **Error**: `GetCompaniesCompanyIdCampaignManagementAccountHoldersAccountHolderIdErrorBody` — **Case A (typed)**
- **Error arms**: `DefaultErrorResponseEntity` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ListDonationCampaignsResponse` | `adyen/models/list_donation_campaigns_response.py` |
| `GetCompaniesCompanyIdCampaignManagementAccountHoldersAccountHolderIdErrorBody` | `adyen/errors/get_companies_company_id_campaign_management_account_holders_account_holder_id_error.py` |
| `DefaultErrorResponseEntity` | `adyen/models/default_error_response_entity.py` |

### client.donation_campaigns.patch_companies_company_id_campaign_management_donation_campaign_id

- **Route**: `PATCH /companies/{companyId}/campaignManagement/{donationCampaignId}`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default9`
- **Signature**: `def patch_companies_company_id_campaign_management_donation_campaign_id(company_id: str, donation_campaign_id: str, *, body: DonationCampaignUpdate | DonationCampaignUpdateDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `company_id`, `donation_campaign_id`
- **Params**: `company_id` — path `companyId` · `donation_campaign_id` — path `donationCampaignId` · `body` — JSON body
- **Returns (parsed)**: `DonationCampaign1`
- **Returns (raw)**: `ApiResult[DonationCampaign1, PatchCompaniesCompanyIdCampaignManagementDonationCampaignIdErrorBody]`
- **Error**: `PatchCompaniesCompanyIdCampaignManagementDonationCampaignIdErrorBody` — **Case A (typed)**
- **Error arms**: `DefaultErrorResponseEntity` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DonationCampaignUpdate` | `adyen/models/donation_campaign_update.py` |
| `DonationCampaignUpdateDict` | `adyen/models/donation_campaign_update.py` |
| `DonationCampaign1` | `adyen/models/donation_campaign1.py` |
| `PatchCompaniesCompanyIdCampaignManagementDonationCampaignIdErrorBody` | `adyen/errors/patch_companies_company_id_campaign_management_donation_campaign_id_error.py` |
| `DefaultErrorResponseEntity` | `adyen/models/default_error_response_entity.py` |

### client.donation_campaigns.post_companies_company_id_campaign_management

- **Route**: `POST /companies/{companyId}/campaignManagement`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default9`
- **Signature**: `def post_companies_company_id_campaign_management(company_id: str, *, body: DonationCampaignRequest | DonationCampaignRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `company_id`
- **Params**: `company_id` — path `companyId` · `body` — JSON body
- **Returns (parsed)**: `DonationCampaign1`
- **Returns (raw)**: `ApiResult[DonationCampaign1, PostCompaniesCompanyIdCampaignManagementErrorBody]`
- **Error**: `PostCompaniesCompanyIdCampaignManagementErrorBody` — **Case A (typed)**
- **Error arms**: `DefaultErrorResponseEntity` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DonationCampaignRequest` | `adyen/models/donation_campaign_request.py` |
| `DonationCampaignRequestDict` | `adyen/models/donation_campaign_request.py` |
| `DonationCampaign1` | `adyen/models/donation_campaign1.py` |
| `PostCompaniesCompanyIdCampaignManagementErrorBody` | `adyen/errors/post_companies_company_id_campaign_management_error.py` |
| `DefaultErrorResponseEntity` | `adyen/models/default_error_response_entity.py` |

### client.donation_campaigns.post_companies_company_id_campaign_management_donation_campaign_id_status_status

- **Route**: `POST /companies/{companyId}/campaignManagement/{donationCampaignId}/status/{status}`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default9`
- **Signature**: `def post_companies_company_id_campaign_management_donation_campaign_id_status_status(company_id: str, donation_campaign_id: str, status: CampaignStatusTransitionOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `company_id`, `donation_campaign_id`, `status`
- **Params**: `company_id` — path `companyId` · `donation_campaign_id` — path `donationCampaignId` · `status` — path
- **Returns (parsed)**: `DonationCampaign1`
- **Returns (raw)**: `ApiResult[DonationCampaign1, PostCompaniesCompanyIdCampaignManagementDonationCampaignIdStatusStatusErrorBody]`
- **Error**: `PostCompaniesCompanyIdCampaignManagementDonationCampaignIdStatusStatusErrorBody` — **Case A (typed)**
- **Error arms**: `DefaultErrorResponseEntity` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CampaignStatusTransitionOrStr` | `adyen/models/enums/campaign_status_transition.py` |
| `DonationCampaign1` | `adyen/models/donation_campaign1.py` |
| `PostCompaniesCompanyIdCampaignManagementDonationCampaignIdStatusStatusErrorBody` | `adyen/errors/post_companies_company_id_campaign_management_donation_campaign_id_status_status_error.py` |
| `DefaultErrorResponseEntity` | `adyen/models/default_error_response_entity.py` |

### client.donation_campaigns.post_companies_company_id_nonprofits

- **Route**: `POST /companies/{companyId}/nonprofits`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default9`
- **Signature**: `def post_companies_company_id_nonprofits(company_id: str, *, search_term: str | None = None, page_number: int | None = None, page_size: int | None = 10, goal: list[str] | None = None, body: ListNonprofitsRequest | ListNonprofitsRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `company_id`
- **Params**: `company_id` — path `companyId` · `search_term` — query `searchTerm` · `page_number` — query `pageNumber` · `page_size` — query `pageSize` · `goal` — query · `body` — JSON body
- **Returns (parsed)**: `ListNonprofitsResponse`
- **Returns (raw)**: `ApiResult[ListNonprofitsResponse, PostCompaniesCompanyIdNonprofitsErrorBody]`
- **Error**: `PostCompaniesCompanyIdNonprofitsErrorBody` — **Case A (typed)**
- **Error arms**: `DefaultErrorResponseEntity` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ListNonprofitsRequest` | `adyen/models/list_nonprofits_request.py` |
| `ListNonprofitsRequestDict` | `adyen/models/list_nonprofits_request.py` |
| `ListNonprofitsResponse` | `adyen/models/list_nonprofits_response.py` |
| `PostCompaniesCompanyIdNonprofitsErrorBody` | `adyen/errors/post_companies_company_id_nonprofits_error.py` |
| `DefaultErrorResponseEntity` | `adyen/models/default_error_response_entity.py` |

