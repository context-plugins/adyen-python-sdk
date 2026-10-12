<!-- Generated file — do not edit; regenerated with the SDK. -->

# LegalEntities — operations

Accessor: `client.legal_entities` · Source: `adyen/apis/legal_entities.py` · 7 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded, and an operation with no table mentions nothing but builtins and those.

### client.legal_entities.get_legal_entities_id

- **Route**: `GET /legalEntities/{id}`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default18`
- **Signature**: `def get_legal_entities_id(id_: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id_`
- **Params**: `id_` — path `id`
- **Returns (parsed)**: `LegalEntity3`
- **Returns (raw)**: `ApiResult[LegalEntity3, GetLegalEntitiesIdErrorBody]`
- **Error**: `GetLegalEntitiesIdErrorBody` — **Case A (typed)**
- **Error arms**: `ServiceError1` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `LegalEntity3` | `adyen/models/legal_entity3.py` |
| `GetLegalEntitiesIdErrorBody` | `adyen/errors/get_legal_entities_id_error.py` |
| `ServiceError1` | `adyen/models/service_error1.py` |

### client.legal_entities.get_legal_entities_id_business_lines

- **Route**: `GET /legalEntities/{id}/businessLines`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default18`
- **Signature**: `def get_legal_entities_id_business_lines(id_: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id_`
- **Params**: `id_` — path `id`
- **Returns (parsed)**: `BusinessLines`
- **Returns (raw)**: `ApiResult[BusinessLines, GetLegalEntitiesIdBusinessLinesErrorBody]`
- **Error**: `GetLegalEntitiesIdBusinessLinesErrorBody` — **Case A (typed)**
- **Error arms**: `ServiceError1` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `BusinessLines` | `adyen/models/business_lines.py` |
| `GetLegalEntitiesIdBusinessLinesErrorBody` | `adyen/errors/get_legal_entities_id_business_lines_error.py` |
| `ServiceError1` | `adyen/models/service_error1.py` |

### client.legal_entities.patch_legal_entities_id

- **Route**: `PATCH /legalEntities/{id}`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default18`
- **Signature**: `def patch_legal_entities_id(id_: str, *, x_requested_verification_code: str | None = None, body: LegalEntityInfo | LegalEntityInfoDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id_`
- **Params**: `id_` — path `id` · `x_requested_verification_code` — header `x-requested-verification-code` · `body` — JSON body
- **Returns (parsed)**: `LegalEntity3`
- **Returns (raw)**: `ApiResult[LegalEntity3, PatchLegalEntitiesIdErrorBody]`
- **Error**: `PatchLegalEntitiesIdErrorBody` — **Case A (typed)**
- **Error arms**: `ServiceError1` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `LegalEntityInfo` | `adyen/models/legal_entity_info.py` |
| `LegalEntityInfoDict` | `adyen/models/legal_entity_info.py` |
| `LegalEntity3` | `adyen/models/legal_entity3.py` |
| `PatchLegalEntitiesIdErrorBody` | `adyen/errors/patch_legal_entities_id_error.py` |
| `ServiceError1` | `adyen/models/service_error1.py` |

### client.legal_entities.post_legal_entities

- **Route**: `POST /legalEntities`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default18`
- **Signature**: `def post_legal_entities(*, x_requested_verification_code: str | None = None, body: LegalEntityInfoRequiredType | LegalEntityInfoRequiredTypeDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `x_requested_verification_code` — header `x-requested-verification-code` · `body` — JSON body
- **Returns (parsed)**: `LegalEntity3`
- **Returns (raw)**: `ApiResult[LegalEntity3, PostLegalEntitiesErrorBody]`
- **Error**: `PostLegalEntitiesErrorBody` — **Case A (typed)**
- **Error arms**: `ServiceError1` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `LegalEntityInfoRequiredType` | `adyen/models/legal_entity_info_required_type.py` |
| `LegalEntityInfoRequiredTypeDict` | `adyen/models/legal_entity_info_required_type.py` |
| `LegalEntity3` | `adyen/models/legal_entity3.py` |
| `PostLegalEntitiesErrorBody` | `adyen/errors/post_legal_entities_error.py` |
| `ServiceError1` | `adyen/models/service_error1.py` |

### client.legal_entities.post_legal_entities_id_check_verification_errors

- **Route**: `POST /legalEntities/{id}/checkVerificationErrors`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default18`
- **Signature**: `def post_legal_entities_id_check_verification_errors(id_: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id_`
- **Params**: `id_` — path `id`
- **Returns (parsed)**: `VerificationErrors`
- **Returns (raw)**: `ApiResult[VerificationErrors, PostLegalEntitiesIdCheckVerificationErrorsErrorBody]`
- **Error**: `PostLegalEntitiesIdCheckVerificationErrorsErrorBody` — **Case A (typed)**
- **Error arms**: `ServiceError1` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `VerificationErrors` | `adyen/models/verification_errors.py` |
| `PostLegalEntitiesIdCheckVerificationErrorsErrorBody` | `adyen/errors/post_legal_entities_id_check_verification_errors_error.py` |
| `ServiceError1` | `adyen/models/service_error1.py` |

### client.legal_entities.post_legal_entities_id_confirm_data_review

- **Route**: `POST /legalEntities/{id}/confirmDataReview`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default18`
- **Signature**: `def post_legal_entities_id_confirm_data_review(id_: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id_`
- **Params**: `id_` — path `id`
- **Returns (parsed)**: `DataReviewConfirmationResponse`
- **Returns (raw)**: `ApiResult[DataReviewConfirmationResponse, PostLegalEntitiesIdConfirmDataReviewErrorBody]`
- **Error**: `PostLegalEntitiesIdConfirmDataReviewErrorBody` — **Case A (typed)**
- **Error arms**: `ServiceError1` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DataReviewConfirmationResponse` | `adyen/models/data_review_confirmation_response.py` |
| `PostLegalEntitiesIdConfirmDataReviewErrorBody` | `adyen/errors/post_legal_entities_id_confirm_data_review_error.py` |
| `ServiceError1` | `adyen/models/service_error1.py` |

### client.legal_entities.post_legal_entities_id_request_periodic_review

- **Route**: `POST /legalEntities/{id}/requestPeriodicReview`
- **Server**: `default18`
- **Signature**: `def post_legal_entities_id_request_periodic_review(id_: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id_`
- **Params**: `id_` — path `id`
- **Returns (parsed)**: `Any`
- **Returns (raw)**: `ApiResult[Any, RawError]`
- **Error**: `RawError` — **Case B**

