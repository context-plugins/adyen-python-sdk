<!-- Generated file — do not edit; regenerated with the SDK. -->

# PaymentLinks — operations

Accessor: `client.payment_links` · Source: `adyen/apis/payment_links.py` · 3 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.payment_links.get_payment_links_link_id

- **Route**: `GET /paymentLinks/{linkId}`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default`
- **Signature**: `def get_payment_links_link_id(link_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `link_id`
- **Params**: `link_id` — path `linkId`
- **Returns (parsed)**: `PaymentLinkResponse`
- **Returns (raw)**: `ApiResult[PaymentLinkResponse, GetPaymentLinksLinkIdErrorBody]`
- **Error**: `GetPaymentLinksLinkIdErrorBody` — **Case A (typed)**
- **Error arms**: `ServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `PaymentLinkResponse` | `adyen/models/payment_link_response.py` |
| `GetPaymentLinksLinkIdErrorBody` | `adyen/errors/get_payment_links_link_id_error.py` |
| `ServiceError` | `adyen/models/service_error.py` |

### client.payment_links.patch_payment_links_link_id

- **Route**: `PATCH /paymentLinks/{linkId}`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default`
- **Signature**: `def patch_payment_links_link_id(link_id: str, *, body: UpdatePaymentLinkRequest | UpdatePaymentLinkRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `link_id`
- **Params**: `link_id` — path `linkId` · `body` — JSON body
- **Returns (parsed)**: `PaymentLinkResponse`
- **Returns (raw)**: `ApiResult[PaymentLinkResponse, PatchPaymentLinksLinkIdErrorBody]`
- **Error**: `PatchPaymentLinksLinkIdErrorBody` — **Case A (typed)**
- **Error arms**: `ServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `UpdatePaymentLinkRequest` | `adyen/models/update_payment_link_request.py` |
| `UpdatePaymentLinkRequestDict` | `adyen/models/update_payment_link_request.py` |
| `PaymentLinkResponse` | `adyen/models/payment_link_response.py` |
| `PatchPaymentLinksLinkIdErrorBody` | `adyen/errors/patch_payment_links_link_id_error.py` |
| `ServiceError` | `adyen/models/service_error.py` |

### client.payment_links.post_payment_links

- **Route**: `POST /paymentLinks`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default`
- **Signature**: `def post_payment_links(*, idempotency_key: str | None = None, body: PaymentLinkRequest | PaymentLinkRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `idempotency_key` — header `Idempotency-Key` · `body` — JSON body
- **Returns (parsed)**: `PaymentLinkResponse`
- **Returns (raw)**: `ApiResult[PaymentLinkResponse, PostPaymentLinksErrorBody]`
- **Error**: `PostPaymentLinksErrorBody` — **Case A (typed)**
- **Error arms**: `ServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `PaymentLinkRequest` | `adyen/models/payment_link_request.py` |
| `PaymentLinkRequestDict` | `adyen/models/payment_link_request.py` |
| `PaymentLinkResponse` | `adyen/models/payment_link_response.py` |
| `PostPaymentLinksErrorBody` | `adyen/errors/post_payment_links_error.py` |
| `ServiceError` | `adyen/models/service_error.py` |

