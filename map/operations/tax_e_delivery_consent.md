<!-- Generated file — do not edit; regenerated with the SDK. -->

# TaxEDeliveryConsent — operations

Accessor: `client.tax_e_delivery_consent` · Source: `adyen/apis/tax_e_delivery_consent.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.tax_e_delivery_consent.post_legal_entities_id_check_tax_electronic_delivery_consent

- **Route**: `POST /legalEntities/{id}/checkTaxElectronicDeliveryConsent`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default18`
- **Signature**: `def post_legal_entities_id_check_tax_electronic_delivery_consent(id_: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id_`
- **Params**: `id_` — path `id`
- **Returns (parsed)**: `CheckTaxElectronicDeliveryConsentResponse`
- **Returns (raw)**: `ApiResult[CheckTaxElectronicDeliveryConsentResponse, PostLegalEntitiesIdCheckTaxElectronicDeliveryConsentErrorBody]`
- **Error**: `PostLegalEntitiesIdCheckTaxElectronicDeliveryConsentErrorBody` — **Case A (typed)**
- **Error arms**: `ServiceError1` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CheckTaxElectronicDeliveryConsentResponse` | `adyen/models/check_tax_electronic_delivery_consent_response.py` |
| `PostLegalEntitiesIdCheckTaxElectronicDeliveryConsentErrorBody` | `adyen/errors/post_legal_entities_id_check_tax_electronic_delivery_consent_error.py` |
| `ServiceError1` | `adyen/models/service_error1.py` |

### client.tax_e_delivery_consent.post_legal_entities_id_set_tax_electronic_delivery_consent

- **Route**: `POST /legalEntities/{id}/setTaxElectronicDeliveryConsent`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default18`
- **Signature**: `def post_legal_entities_id_set_tax_electronic_delivery_consent(id_: str, *, body: SetTaxElectronicDeliveryConsentRequest | SetTaxElectronicDeliveryConsentRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id_`
- **Params**: `id_` — path `id` · `body` — JSON body
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, PostLegalEntitiesIdSetTaxElectronicDeliveryConsentErrorBody]`
- **Error**: `PostLegalEntitiesIdSetTaxElectronicDeliveryConsentErrorBody` — **Case A (typed)**
- **Error arms**: `ServiceError1` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SetTaxElectronicDeliveryConsentRequest` | `adyen/models/set_tax_electronic_delivery_consent_request.py` |
| `SetTaxElectronicDeliveryConsentRequestDict` | `adyen/models/set_tax_electronic_delivery_consent_request.py` |
| `PostLegalEntitiesIdSetTaxElectronicDeliveryConsentErrorBody` | `adyen/errors/post_legal_entities_id_set_tax_electronic_delivery_consent_error.py` |
| `ServiceError1` | `adyen/models/service_error1.py` |

