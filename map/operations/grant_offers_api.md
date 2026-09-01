<!-- Generated file — do not edit; regenerated with the SDK. -->

# GrantOffersApi — operations

Accessor: `client.grant_offers_api` · Source: `adyen/apis/grant_offers_api.py` · 4 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.grant_offers_api.get_grant_offers

- **Route**: `GET /grantOffers`
- **Auth**: `client_key` OR `basic_auth` OR `api_key_auth`
- **Server**: `default13`
- **Signature**: `def get_grant_offers(account_holder_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_holder_id`
- **Params**: `account_holder_id` — query `accountHolderId`
- **Returns (parsed)**: `GrantOffers`
- **Returns (raw)**: `ApiResult[GrantOffers, GetGrantOffersErrorBody]`
- **Error**: `GetGrantOffersErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `GrantOffers` | `adyen/models/grant_offers.py` |
| `GetGrantOffersErrorBody` | `adyen/errors/get_grant_offers_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.grant_offers_api.get_grant_offers_grant_offer_id

- **Route**: `GET /grantOffers/{grantOfferId}`
- **Auth**: `client_key` OR `basic_auth` OR `api_key_auth`
- **Server**: `default13`
- **Signature**: `def get_grant_offers_grant_offer_id(grant_offer_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `grant_offer_id`
- **Params**: `grant_offer_id` — path `grantOfferId`
- **Returns (parsed)**: `GrantOffer`
- **Returns (raw)**: `ApiResult[GrantOffer, GetGrantOffersGrantOfferIdErrorBody]`
- **Error**: `GetGrantOffersGrantOfferIdErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `GrantOffer` | `adyen/models/grant_offer.py` |
| `GetGrantOffersGrantOfferIdErrorBody` | `adyen/errors/get_grant_offers_grant_offer_id_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.grant_offers_api.get_grant_offers_id

- **Route**: `GET /grantOffers/{id}`
- **Server**: `default15`
- **Signature**: `def get_grant_offers_id(id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`
- **Params**: `id` — path
- **Returns (parsed)**: `GrantOffer1`
- **Returns (raw)**: `ApiResult[GrantOffer1, GetGrantOffersIdErrorBody]`
- **Error**: `GetGrantOffersIdErrorBody` — **Case A (typed)**
- **Error arms**: `DefaultErrorResponseEntity` [404, 422] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `GrantOffer1` | `adyen/models/grant_offer1.py` |
| `GetGrantOffersIdErrorBody` | `adyen/errors/get_grant_offers_id_error.py` |
| `DefaultErrorResponseEntity` | `adyen/models/default_error_response_entity.py` |

### client.grant_offers_api.get_grant_offers1

- **Route**: `GET /grantOffers`
- **Server**: `default15`
- **Signature**: `def get_grant_offers1(account_holder_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_holder_id`
- **Params**: `account_holder_id` — query `accountHolderId`
- **Returns (parsed)**: `GrantOffers`
- **Returns (raw)**: `ApiResult[GrantOffers, GetGrantOffers1ErrorBody]`
- **Error**: `GetGrantOffers1ErrorBody` — **Case A (typed)**
- **Error arms**: `DefaultErrorResponseEntity` [404, 422] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `GrantOffers` | `adyen/models/grant_offers.py` |
| `GetGrantOffers1ErrorBody` | `adyen/errors/get_grant_offers1_error.py` |
| `DefaultErrorResponseEntity` | `adyen/models/default_error_response_entity.py` |

