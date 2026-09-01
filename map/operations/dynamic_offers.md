<!-- Generated file — do not edit; regenerated with the SDK. -->

# DynamicOffers — operations

Accessor: `client.dynamic_offers` · Source: `adyen/apis/dynamic_offers.py` · 3 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.dynamic_offers.get_dynamic_offers

- **Route**: `GET /dynamicOffers`
- **Server**: `default15`
- **Signature**: `def get_dynamic_offers(account_holder_id: str, *, financing_type: FinancingTypeOrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_holder_id`
- **Params**: `account_holder_id` — query `accountHolderId` · `financing_type` — query `financingType`
- **Returns (parsed)**: `GetDynamicOffersResponse`
- **Returns (raw)**: `ApiResult[GetDynamicOffersResponse, GetDynamicOffersErrorBody]`
- **Error**: `GetDynamicOffersErrorBody` — **Case A (typed)**
- **Error arms**: `DefaultErrorResponseEntity` [422] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FinancingTypeOrStr` | `adyen/models/enums/financing_type.py` |
| `GetDynamicOffersResponse` | `adyen/models/get_dynamic_offers_response.py` |
| `GetDynamicOffersErrorBody` | `adyen/errors/get_dynamic_offers_error.py` |
| `DefaultErrorResponseEntity` | `adyen/models/default_error_response_entity.py` |

### client.dynamic_offers.post_dynamic_offers_id_calculate

- **Route**: `POST /dynamicOffers/{id}/calculate`
- **Server**: `default15`
- **Signature**: `def post_dynamic_offers_id_calculate(id: str, *, body: CalculateGrantOfferRequest | CalculateGrantOfferRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`
- **Params**: `id` — path · `body` — JSON body
- **Returns (parsed)**: `CalculatedGrantOffer`
- **Returns (raw)**: `ApiResult[CalculatedGrantOffer, PostDynamicOffersIdCalculateErrorBody]`
- **Error**: `PostDynamicOffersIdCalculateErrorBody` — **Case A (typed)**
- **Error arms**: `DefaultErrorResponseEntity` [422] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CalculateGrantOfferRequest` | `adyen/models/calculate_grant_offer_request.py` |
| `CalculateGrantOfferRequestDict` | `adyen/models/calculate_grant_offer_request.py` |
| `CalculatedGrantOffer` | `adyen/models/calculated_grant_offer.py` |
| `PostDynamicOffersIdCalculateErrorBody` | `adyen/errors/post_dynamic_offers_id_calculate_error.py` |
| `DefaultErrorResponseEntity` | `adyen/models/default_error_response_entity.py` |

### client.dynamic_offers.post_dynamic_offers_id_grant_offer

- **Route**: `POST /dynamicOffers/{id}/grantOffer`
- **Server**: `default15`
- **Signature**: `def post_dynamic_offers_id_grant_offer(id: str, *, body: CreateGrantOfferRequest | CreateGrantOfferRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`
- **Params**: `id` — path · `body` — JSON body
- **Returns (parsed)**: `GrantOffer1`
- **Returns (raw)**: `ApiResult[GrantOffer1, PostDynamicOffersIdGrantOfferErrorBody]`
- **Error**: `PostDynamicOffersIdGrantOfferErrorBody` — **Case A (typed)**
- **Error arms**: `DefaultErrorResponseEntity` [422] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CreateGrantOfferRequest` | `adyen/models/create_grant_offer_request.py` |
| `CreateGrantOfferRequestDict` | `adyen/models/create_grant_offer_request.py` |
| `GrantOffer1` | `adyen/models/grant_offer1.py` |
| `PostDynamicOffersIdGrantOfferErrorBody` | `adyen/errors/post_dynamic_offers_id_grant_offer_error.py` |
| `DefaultErrorResponseEntity` | `adyen/models/default_error_response_entity.py` |

