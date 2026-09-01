<!-- Generated file — do not edit; regenerated with the SDK. -->

# NetworkTokens — operations

Accessor: `client.network_tokens` · Source: `adyen/apis/network_tokens.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.network_tokens.get_network_tokens_network_token_id

- **Route**: `GET /networkTokens/{networkTokenId}`
- **Auth**: `client_key` OR `basic_auth` OR `api_key_auth`
- **Server**: `default13`
- **Signature**: `def get_network_tokens_network_token_id(network_token_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `network_token_id`
- **Params**: `network_token_id` — path `networkTokenId`
- **Returns (parsed)**: `GetNetworkTokenResponse`
- **Returns (raw)**: `ApiResult[GetNetworkTokenResponse, GetNetworkTokensNetworkTokenIdErrorBody]`
- **Error**: `GetNetworkTokensNetworkTokenIdErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `GetNetworkTokenResponse` | `adyen/models/get_network_token_response.py` |
| `GetNetworkTokensNetworkTokenIdErrorBody` | `adyen/errors/get_network_tokens_network_token_id_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.network_tokens.patch_network_tokens_network_token_id

- **Route**: `PATCH /networkTokens/{networkTokenId}`
- **Auth**: `client_key` OR `basic_auth` OR `api_key_auth`
- **Server**: `default13`
- **Signature**: `def patch_network_tokens_network_token_id(network_token_id: str, *, body: UpdateNetworkTokenRequest | UpdateNetworkTokenRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `network_token_id`
- **Params**: `network_token_id` — path `networkTokenId` · `body` — JSON body
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, PatchNetworkTokensNetworkTokenIdErrorBody]`
- **Error**: `PatchNetworkTokensNetworkTokenIdErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `UpdateNetworkTokenRequest` | `adyen/models/update_network_token_request.py` |
| `UpdateNetworkTokenRequestDict` | `adyen/models/update_network_token_request.py` |
| `PatchNetworkTokensNetworkTokenIdErrorBody` | `adyen/errors/patch_network_tokens_network_token_id_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

