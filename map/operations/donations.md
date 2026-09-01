<!-- Generated file — do not edit; regenerated with the SDK. -->

# Donations — operations

Accessor: `client.donations` · Source: `adyen/apis/donations.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.donations.post_donation_campaigns

- **Route**: `POST /donationCampaigns`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default`
- **Signature**: `def post_donation_campaigns(*, idempotency_key: str | None = None, body: DonationCampaignsRequest | DonationCampaignsRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `idempotency_key` — header `Idempotency-Key` · `body` — JSON body
- **Returns (parsed)**: `DonationCampaignsResponse`
- **Returns (raw)**: `ApiResult[DonationCampaignsResponse, PostDonationCampaignsErrorBody]`
- **Error**: `PostDonationCampaignsErrorBody` — **Case A (typed)**
- **Error arms**: `ServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DonationCampaignsRequest` | `adyen/models/donation_campaigns_request.py` |
| `DonationCampaignsRequestDict` | `adyen/models/donation_campaigns_request.py` |
| `DonationCampaignsResponse` | `adyen/models/donation_campaigns_response.py` |
| `PostDonationCampaignsErrorBody` | `adyen/errors/post_donation_campaigns_error.py` |
| `ServiceError` | `adyen/models/service_error.py` |

### client.donations.post_donations

- **Route**: `POST /donations`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default`
- **Signature**: `def post_donations(*, idempotency_key: str | None = None, body: DonationPaymentRequest | DonationPaymentRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `idempotency_key` — header `Idempotency-Key` · `body` — JSON body
- **Returns (parsed)**: `DonationPaymentResponse`
- **Returns (raw)**: `ApiResult[DonationPaymentResponse, PostDonationsErrorBody]`
- **Error**: `PostDonationsErrorBody` — **Case A (typed)**
- **Error arms**: `ServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DonationPaymentRequest` | `adyen/models/donation_payment_request.py` |
| `DonationPaymentRequestDict` | `adyen/models/donation_payment_request.py` |
| `DonationPaymentResponse` | `adyen/models/donation_payment_response.py` |
| `PostDonationsErrorBody` | `adyen/errors/post_donations_error.py` |
| `ServiceError` | `adyen/models/service_error.py` |

