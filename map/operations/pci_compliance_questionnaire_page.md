<!-- Generated file — do not edit; regenerated with the SDK. -->

# PciComplianceQuestionnairePage — operations

Accessor: `client.pci_compliance_questionnaire_page` · Source: `adyen/apis/pci_compliance_questionnaire_page.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.pci_compliance_questionnaire_page.post_get_pci_questionnaire_url

- **Route**: `POST /getPciQuestionnaireUrl`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default19`
- **Signature**: `def post_get_pci_questionnaire_url(*, body: GetPciUrlRequest | GetPciUrlRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `GetPciUrlResponse`
- **Returns (raw)**: `ApiResult[GetPciUrlResponse, PostGetPciQuestionnaireUrlErrorBody]`
- **Error**: `PostGetPciQuestionnaireUrlErrorBody` — **Case A (typed)**
- **Error arms**: `ServiceError1` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `GetPciUrlRequest` | `adyen/models/get_pci_url_request.py` |
| `GetPciUrlRequestDict` | `adyen/models/get_pci_url_request.py` |
| `GetPciUrlResponse` | `adyen/models/get_pci_url_response.py` |
| `PostGetPciQuestionnaireUrlErrorBody` | `adyen/errors/post_get_pci_questionnaire_url_error.py` |
| `ServiceError1` | `adyen/models/service_error1.py` |

