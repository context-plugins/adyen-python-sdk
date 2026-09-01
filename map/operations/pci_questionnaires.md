<!-- Generated file — do not edit; regenerated with the SDK. -->

# PciQuestionnaires — operations

Accessor: `client.pci_questionnaires` · Source: `adyen/apis/pci_questionnaires.py` · 5 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.pci_questionnaires.get_legal_entities_id_pci_questionnaires

- **Route**: `GET /legalEntities/{id}/pciQuestionnaires`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default18`
- **Signature**: `def get_legal_entities_id_pci_questionnaires(id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`
- **Params**: `id` — path
- **Returns (parsed)**: `GetPciQuestionnaireInfosResponse`
- **Returns (raw)**: `ApiResult[GetPciQuestionnaireInfosResponse, GetLegalEntitiesIdPciQuestionnairesErrorBody]`
- **Error**: `GetLegalEntitiesIdPciQuestionnairesErrorBody` — **Case A (typed)**
- **Error arms**: `ServiceError1` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `GetPciQuestionnaireInfosResponse` | `adyen/models/get_pci_questionnaire_infos_response.py` |
| `GetLegalEntitiesIdPciQuestionnairesErrorBody` | `adyen/errors/get_legal_entities_id_pci_questionnaires_error.py` |
| `ServiceError1` | `adyen/models/service_error1.py` |

### client.pci_questionnaires.get_legal_entities_id_pci_questionnaires_pciid

- **Route**: `GET /legalEntities/{id}/pciQuestionnaires/{pciid}`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default18`
- **Signature**: `def get_legal_entities_id_pci_questionnaires_pciid(id: str, pciid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`, `pciid`
- **Params**: `id` — path · `pciid` — path
- **Returns (parsed)**: `GetPciQuestionnaireResponse`
- **Returns (raw)**: `ApiResult[GetPciQuestionnaireResponse, GetLegalEntitiesIdPciQuestionnairesPciidErrorBody]`
- **Error**: `GetLegalEntitiesIdPciQuestionnairesPciidErrorBody` — **Case A (typed)**
- **Error arms**: `ServiceError1` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `GetPciQuestionnaireResponse` | `adyen/models/get_pci_questionnaire_response.py` |
| `GetLegalEntitiesIdPciQuestionnairesPciidErrorBody` | `adyen/errors/get_legal_entities_id_pci_questionnaires_pciid_error.py` |
| `ServiceError1` | `adyen/models/service_error1.py` |

### client.pci_questionnaires.post_legal_entities_id_pci_questionnaires_generate_pci_templates

- **Route**: `POST /legalEntities/{id}/pciQuestionnaires/generatePciTemplates`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default18`
- **Signature**: `def post_legal_entities_id_pci_questionnaires_generate_pci_templates(id: str, *, body: GeneratePciDescriptionRequest | GeneratePciDescriptionRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`
- **Params**: `id` — path · `body` — JSON body
- **Returns (parsed)**: `GeneratePciDescriptionResponse`
- **Returns (raw)**: `ApiResult[GeneratePciDescriptionResponse, PostLegalEntitiesIdPciQuestionnairesGeneratePciTemplatesErrorBody]`
- **Error**: `PostLegalEntitiesIdPciQuestionnairesGeneratePciTemplatesErrorBody` — **Case A (typed)**
- **Error arms**: `ServiceError1` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `GeneratePciDescriptionRequest` | `adyen/models/generate_pci_description_request.py` |
| `GeneratePciDescriptionRequestDict` | `adyen/models/generate_pci_description_request.py` |
| `GeneratePciDescriptionResponse` | `adyen/models/generate_pci_description_response.py` |
| `PostLegalEntitiesIdPciQuestionnairesGeneratePciTemplatesErrorBody` | `adyen/errors/post_legal_entities_id_pci_questionnaires_generate_pci_templates_error.py` |
| `ServiceError1` | `adyen/models/service_error1.py` |

### client.pci_questionnaires.post_legal_entities_id_pci_questionnaires_sign_pci_templates

- **Route**: `POST /legalEntities/{id}/pciQuestionnaires/signPciTemplates`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default18`
- **Signature**: `def post_legal_entities_id_pci_questionnaires_sign_pci_templates(id: str, *, body: PciSigningRequest | PciSigningRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`
- **Params**: `id` — path · `body` — JSON body
- **Returns (parsed)**: `PciSigningResponse`
- **Returns (raw)**: `ApiResult[PciSigningResponse, PostLegalEntitiesIdPciQuestionnairesSignPciTemplatesErrorBody]`
- **Error**: `PostLegalEntitiesIdPciQuestionnairesSignPciTemplatesErrorBody` — **Case A (typed)**
- **Error arms**: `ServiceError1` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `PciSigningRequest` | `adyen/models/pci_signing_request.py` |
| `PciSigningRequestDict` | `adyen/models/pci_signing_request.py` |
| `PciSigningResponse` | `adyen/models/pci_signing_response.py` |
| `PostLegalEntitiesIdPciQuestionnairesSignPciTemplatesErrorBody` | `adyen/errors/post_legal_entities_id_pci_questionnaires_sign_pci_templates_error.py` |
| `ServiceError1` | `adyen/models/service_error1.py` |

### client.pci_questionnaires.post_legal_entities_id_pci_questionnaires_signing_required

- **Route**: `POST /legalEntities/{id}/pciQuestionnaires/signingRequired`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default18`
- **Signature**: `def post_legal_entities_id_pci_questionnaires_signing_required(id: str, *, body: CalculatePciStatusRequest | CalculatePciStatusRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`
- **Params**: `id` — path · `body` — JSON body
- **Returns (parsed)**: `CalculatePciStatusResponse`
- **Returns (raw)**: `ApiResult[CalculatePciStatusResponse, PostLegalEntitiesIdPciQuestionnairesSigningRequiredErrorBody]`
- **Error**: `PostLegalEntitiesIdPciQuestionnairesSigningRequiredErrorBody` — **Case A (typed)**
- **Error arms**: `ServiceError1` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CalculatePciStatusRequest` | `adyen/models/calculate_pci_status_request.py` |
| `CalculatePciStatusRequestDict` | `adyen/models/calculate_pci_status_request.py` |
| `CalculatePciStatusResponse` | `adyen/models/calculate_pci_status_response.py` |
| `PostLegalEntitiesIdPciQuestionnairesSigningRequiredErrorBody` | `adyen/errors/post_legal_entities_id_pci_questionnaires_signing_required_error.py` |
| `ServiceError1` | `adyen/models/service_error1.py` |

