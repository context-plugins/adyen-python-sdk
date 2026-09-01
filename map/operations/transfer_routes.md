<!-- Generated file — do not edit; regenerated with the SDK. -->

# TransferRoutes — operations

Accessor: `client.transfer_routes` · Source: `adyen/apis/transfer_routes.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.transfer_routes.post_transfer_routes_calculate

- **Route**: `POST /transferRoutes/calculate`
- **Auth**: `client_key` OR `basic_auth` OR `api_key_auth`
- **Server**: `default13`
- **Signature**: `def post_transfer_routes_calculate(*, body: TransferRouteRequest | TransferRouteRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `TransferRouteResponse`
- **Returns (raw)**: `ApiResult[TransferRouteResponse, PostTransferRoutesCalculateErrorBody]`
- **Error**: `PostTransferRoutesCalculateErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `TransferRouteRequest` | `adyen/models/transfer_route_request.py` |
| `TransferRouteRequestDict` | `adyen/models/transfer_route_request.py` |
| `TransferRouteResponse` | `adyen/models/transfer_route_response.py` |
| `PostTransferRoutesCalculateErrorBody` | `adyen/errors/post_transfer_routes_calculate_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

