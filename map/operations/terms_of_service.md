<!-- Generated file — do not edit; regenerated with the SDK. -->

# TermsOfService — operations

Accessor: `client.terms_of_service` · Source: `adyen/apis/terms_of_service.py` · 5 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.terms_of_service.get_legal_entities_id_accepted_terms_of_service_document_termsofserviceacceptancereference

- **Route**: `GET /legalEntities/{id}/acceptedTermsOfServiceDocument/{termsofserviceacceptancereference}`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default18`
- **Signature**: `def get_legal_entities_id_accepted_terms_of_service_document_termsofserviceacceptancereference(id_: str, termsofserviceacceptancereference: str, *, terms_of_service_document_format: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id_`, `termsofserviceacceptancereference`
- **Params**: `id_` — path `id` · `termsofserviceacceptancereference` — path · `terms_of_service_document_format` — query `termsOfServiceDocumentFormat`
- **Returns (parsed)**: `GetAcceptedTermsOfServiceDocumentResponse`
- **Returns (raw)**: `ApiResult[GetAcceptedTermsOfServiceDocumentResponse, GetLegalEntitiesIdAcceptedTermsOfServiceDocumentTermsofserviceacceptancereferenceErrorBody]`
- **Error**: `GetLegalEntitiesIdAcceptedTermsOfServiceDocumentTermsofserviceacceptancereferenceErrorBody` — **Case A (typed)**
- **Error arms**: `ServiceError1` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `GetAcceptedTermsOfServiceDocumentResponse` | `adyen/models/get_accepted_terms_of_service_document_response.py` |
| `GetLegalEntitiesIdAcceptedTermsOfServiceDocumentTermsofserviceacceptancereferenceErrorBody` | `adyen/errors/get_legal_entities_id_accepted_terms_of_service_document_termsofserviceacceptancereference_error.py` |
| `ServiceError1` | `adyen/models/service_error1.py` |

### client.terms_of_service.get_legal_entities_id_terms_of_service_acceptance_infos

- **Route**: `GET /legalEntities/{id}/termsOfServiceAcceptanceInfos`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default18`
- **Signature**: `def get_legal_entities_id_terms_of_service_acceptance_infos(id_: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id_`
- **Params**: `id_` — path `id`
- **Returns (parsed)**: `GetTermsOfServiceAcceptanceInfosResponse`
- **Returns (raw)**: `ApiResult[GetTermsOfServiceAcceptanceInfosResponse, GetLegalEntitiesIdTermsOfServiceAcceptanceInfosErrorBody]`
- **Error**: `GetLegalEntitiesIdTermsOfServiceAcceptanceInfosErrorBody` — **Case A (typed)**
- **Error arms**: `ServiceError1` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `GetTermsOfServiceAcceptanceInfosResponse` | `adyen/models/get_terms_of_service_acceptance_infos_response.py` |
| `GetLegalEntitiesIdTermsOfServiceAcceptanceInfosErrorBody` | `adyen/errors/get_legal_entities_id_terms_of_service_acceptance_infos_error.py` |
| `ServiceError1` | `adyen/models/service_error1.py` |

### client.terms_of_service.get_legal_entities_id_terms_of_service_status

- **Route**: `GET /legalEntities/{id}/termsOfServiceStatus`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default18`
- **Signature**: `def get_legal_entities_id_terms_of_service_status(id_: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id_`
- **Params**: `id_` — path `id`
- **Returns (parsed)**: `CalculateTermsOfServiceStatusResponse`
- **Returns (raw)**: `ApiResult[CalculateTermsOfServiceStatusResponse, GetLegalEntitiesIdTermsOfServiceStatusErrorBody]`
- **Error**: `GetLegalEntitiesIdTermsOfServiceStatusErrorBody` — **Case A (typed)**
- **Error arms**: `ServiceError1` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CalculateTermsOfServiceStatusResponse` | `adyen/models/calculate_terms_of_service_status_response.py` |
| `GetLegalEntitiesIdTermsOfServiceStatusErrorBody` | `adyen/errors/get_legal_entities_id_terms_of_service_status_error.py` |
| `ServiceError1` | `adyen/models/service_error1.py` |

### client.terms_of_service.patch_legal_entities_id_terms_of_service_termsofservicedocumentid

- **Route**: `PATCH /legalEntities/{id}/termsOfService/{termsofservicedocumentid}`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default18`
- **Signature**: `def patch_legal_entities_id_terms_of_service_termsofservicedocumentid(id_: str, termsofservicedocumentid: str, *, body: AcceptTermsOfServiceRequest | AcceptTermsOfServiceRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id_`, `termsofservicedocumentid`
- **Params**: `id_` — path `id` · `termsofservicedocumentid` — path · `body` — JSON body
- **Returns (parsed)**: `AcceptTermsOfServiceResponse`
- **Returns (raw)**: `ApiResult[AcceptTermsOfServiceResponse, PatchLegalEntitiesIdTermsOfServiceTermsofservicedocumentidErrorBody]`
- **Error**: `PatchLegalEntitiesIdTermsOfServiceTermsofservicedocumentidErrorBody` — **Case A (typed)**
- **Error arms**: `ServiceError1` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `AcceptTermsOfServiceRequest` | `adyen/models/accept_terms_of_service_request.py` |
| `AcceptTermsOfServiceRequestDict` | `adyen/models/accept_terms_of_service_request.py` |
| `AcceptTermsOfServiceResponse` | `adyen/models/accept_terms_of_service_response.py` |
| `PatchLegalEntitiesIdTermsOfServiceTermsofservicedocumentidErrorBody` | `adyen/errors/patch_legal_entities_id_terms_of_service_termsofservicedocumentid_error.py` |
| `ServiceError1` | `adyen/models/service_error1.py` |

### client.terms_of_service.post_legal_entities_id_terms_of_service

- **Route**: `POST /legalEntities/{id}/termsOfService`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default18`
- **Signature**: `def post_legal_entities_id_terms_of_service(id_: str, *, body: GetTermsOfServiceDocumentRequest | GetTermsOfServiceDocumentRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id_`
- **Params**: `id_` — path `id` · `body` — JSON body
- **Returns (parsed)**: `GetTermsOfServiceDocumentResponse`
- **Returns (raw)**: `ApiResult[GetTermsOfServiceDocumentResponse, PostLegalEntitiesIdTermsOfServiceErrorBody]`
- **Error**: `PostLegalEntitiesIdTermsOfServiceErrorBody` — **Case A (typed)**
- **Error arms**: `ServiceError1` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `GetTermsOfServiceDocumentRequest` | `adyen/models/get_terms_of_service_document_request.py` |
| `GetTermsOfServiceDocumentRequestDict` | `adyen/models/get_terms_of_service_document_request.py` |
| `GetTermsOfServiceDocumentResponse` | `adyen/models/get_terms_of_service_document_response.py` |
| `PostLegalEntitiesIdTermsOfServiceErrorBody` | `adyen/errors/post_legal_entities_id_terms_of_service_error.py` |
| `ServiceError1` | `adyen/models/service_error1.py` |

