<!-- Generated file — do not edit; regenerated with the SDK. -->

# TransferLimitsBalancePlatformLevel — operations

Accessor: `client.transfer_limits_balance_platform_level` · Source: `adyen/apis/transfer_limits_balance_platform_level.py` · 4 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.transfer_limits_balance_platform_level.delete_balance_platforms_id_transfer_limits_transfer_limit_id

- **Route**: `DELETE /balancePlatforms/{id}/transferLimits/{transferLimitId}`
- **Server**: `default13`
- **Signature**: `def delete_balance_platforms_id_transfer_limits_transfer_limit_id(id_: str, transfer_limit_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id_`, `transfer_limit_id`
- **Params**: `id_` — path `id` · `transfer_limit_id` — path `transferLimitId`
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, DeleteBalancePlatformsIdTransferLimitsTransferLimitIdErrorBody]`
- **Error**: `DeleteBalancePlatformsIdTransferLimitsTransferLimitIdErrorBody` — **Case A (typed)**
- **Error arms**: `DefaultErrorResponseEntity` [404, 422] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DeleteBalancePlatformsIdTransferLimitsTransferLimitIdErrorBody` | `adyen/errors/delete_balance_platforms_id_transfer_limits_transfer_limit_id_error.py` |
| `DefaultErrorResponseEntity` | `adyen/models/default_error_response_entity.py` |

### client.transfer_limits_balance_platform_level.get_balance_platforms_id_transfer_limits

- **Route**: `GET /balancePlatforms/{id}/transferLimits`
- **Server**: `default13`
- **Signature**: `def get_balance_platforms_id_transfer_limits(id_: str, *, scope: ScopeOrStr | None = None, transfer_type: TransferTypeOrStr | None = None, status: LimitStatusOrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id_`
- **Params**: `id_` — path `id` · `scope` — query · `transfer_type` — query `transferType` · `status` — query
- **Returns (parsed)**: `TransferLimitListResponse`
- **Returns (raw)**: `ApiResult[TransferLimitListResponse, GetBalancePlatformsIdTransferLimitsErrorBody]`
- **Error**: `GetBalancePlatformsIdTransferLimitsErrorBody` — **Case A (typed)**
- **Error arms**: `DefaultErrorResponseEntity` [404, 422] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ScopeOrStr` | `adyen/models/enums/scope.py` |
| `TransferTypeOrStr` | `adyen/models/enums/transfer_type.py` |
| `LimitStatusOrStr` | `adyen/models/enums/limit_status.py` |
| `TransferLimitListResponse` | `adyen/models/transfer_limit_list_response.py` |
| `GetBalancePlatformsIdTransferLimitsErrorBody` | `adyen/errors/get_balance_platforms_id_transfer_limits_error.py` |
| `DefaultErrorResponseEntity` | `adyen/models/default_error_response_entity.py` |

### client.transfer_limits_balance_platform_level.get_balance_platforms_id_transfer_limits_transfer_limit_id

- **Route**: `GET /balancePlatforms/{id}/transferLimits/{transferLimitId}`
- **Server**: `default13`
- **Signature**: `def get_balance_platforms_id_transfer_limits_transfer_limit_id(id_: str, transfer_limit_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id_`, `transfer_limit_id`
- **Params**: `id_` — path `id` · `transfer_limit_id` — path `transferLimitId`
- **Returns (parsed)**: `TransferLimit`
- **Returns (raw)**: `ApiResult[TransferLimit, GetBalancePlatformsIdTransferLimitsTransferLimitIdErrorBody]`
- **Error**: `GetBalancePlatformsIdTransferLimitsTransferLimitIdErrorBody` — **Case A (typed)**
- **Error arms**: `DefaultErrorResponseEntity` [404, 422] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `TransferLimit` | `adyen/models/transfer_limit.py` |
| `GetBalancePlatformsIdTransferLimitsTransferLimitIdErrorBody` | `adyen/errors/get_balance_platforms_id_transfer_limits_transfer_limit_id_error.py` |
| `DefaultErrorResponseEntity` | `adyen/models/default_error_response_entity.py` |

### client.transfer_limits_balance_platform_level.post_balance_platforms_id_transfer_limits

- **Route**: `POST /balancePlatforms/{id}/transferLimits`
- **Server**: `default13`
- **Signature**: `def post_balance_platforms_id_transfer_limits(id_: str, body: CreateTransferLimitRequest | CreateTransferLimitRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id_`, `body`
- **Params**: `id_` — path `id` · `body` — JSON body
- **Returns (parsed)**: `TransferLimit`
- **Returns (raw)**: `ApiResult[TransferLimit, PostBalancePlatformsIdTransferLimitsErrorBody]`
- **Error**: `PostBalancePlatformsIdTransferLimitsErrorBody` — **Case A (typed)**
- **Error arms**: `DefaultErrorResponseEntity` [404, 422] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CreateTransferLimitRequest` | `adyen/models/create_transfer_limit_request.py` |
| `CreateTransferLimitRequestDict` | `adyen/models/create_transfer_limit_request.py` |
| `TransferLimit` | `adyen/models/transfer_limit.py` |
| `PostBalancePlatformsIdTransferLimitsErrorBody` | `adyen/errors/post_balance_platforms_id_transfer_limits_error.py` |
| `DefaultErrorResponseEntity` | `adyen/models/default_error_response_entity.py` |

