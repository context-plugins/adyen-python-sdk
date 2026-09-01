<!-- Generated file — do not edit; regenerated with the SDK. -->

# ScaAssociationManagement — operations

Accessor: `client.sca_association_management` · Source: `adyen/apis/sca_association_management.py` · 3 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.sca_association_management.delete_sca_associations

- **Route**: `DELETE /scaAssociations`
- **Server**: `default13`
- **Signature**: `def delete_sca_associations(www_authenticate: str, *, body: RemoveAssociationRequest | RemoveAssociationRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `www_authenticate`
- **Params**: `www_authenticate` — header `WWW-Authenticate` · `body` — JSON body
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, DeleteScaAssociationsErrorBody]`
- **Error**: `DeleteScaAssociationsErrorBody` — **Case A (typed)**
- **Error arms**: `DefaultErrorResponseEntity` [401, 403, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `RemoveAssociationRequest` | `adyen/models/remove_association_request.py` |
| `RemoveAssociationRequestDict` | `adyen/models/remove_association_request.py` |
| `DeleteScaAssociationsErrorBody` | `adyen/errors/delete_sca_associations_error.py` |
| `DefaultErrorResponseEntity` | `adyen/models/default_error_response_entity.py` |

### client.sca_association_management.get_sca_associations

- **Route**: `GET /scaAssociations`
- **Server**: `default13`
- **Signature**: `def get_sca_associations(entity_type: ScaEntityTypeOrStr, entity_id: str, page_size: int, page_number: int, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `entity_type`, `entity_id`, `page_size`, `page_number`
- **Params**: `entity_type` — query `entityType` · `entity_id` — query `entityId` · `page_size` — query `pageSize` · `page_number` — query `pageNumber`
- **Returns (parsed)**: `ListAssociationsResponse`
- **Returns (raw)**: `ApiResult[ListAssociationsResponse, GetScaAssociationsErrorBody]`
- **Error**: `GetScaAssociationsErrorBody` — **Case A (typed)**
- **Error arms**: `DefaultErrorResponseEntity` [400, 401, 403, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ScaEntityTypeOrStr` | `adyen/models/enums/sca_entity_type.py` |
| `ListAssociationsResponse` | `adyen/models/list_associations_response.py` |
| `GetScaAssociationsErrorBody` | `adyen/errors/get_sca_associations_error.py` |
| `DefaultErrorResponseEntity` | `adyen/models/default_error_response_entity.py` |

### client.sca_association_management.patch_sca_associations

- **Route**: `PATCH /scaAssociations`
- **Server**: `default13`
- **Signature**: `def patch_sca_associations(www_authenticate: str, *, body: ApproveAssociationRequest | ApproveAssociationRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `www_authenticate`
- **Params**: `www_authenticate` — header `WWW-Authenticate` · `body` — JSON body
- **Returns (parsed)**: `ApproveAssociationResponse`
- **Returns (raw)**: `ApiResult[ApproveAssociationResponse, PatchScaAssociationsErrorBody]`
- **Error**: `PatchScaAssociationsErrorBody` — **Case A (typed)**
- **Error arms**: `DefaultErrorResponseEntity` [401, 403, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ApproveAssociationRequest` | `adyen/models/approve_association_request.py` |
| `ApproveAssociationRequestDict` | `adyen/models/approve_association_request.py` |
| `ApproveAssociationResponse` | `adyen/models/approve_association_response.py` |
| `PatchScaAssociationsErrorBody` | `adyen/errors/patch_sca_associations_error.py` |
| `DefaultErrorResponseEntity` | `adyen/models/default_error_response_entity.py` |

