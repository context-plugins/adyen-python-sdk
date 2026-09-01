<!-- Generated file — do not edit; regenerated with the SDK. -->

# BankAccountValidation — operations

Accessor: `client.bank_account_validation` · Source: `adyen/apis/bank_account_validation.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.bank_account_validation.post_validate_bank_account_identification

- **Route**: `POST /validateBankAccountIdentification`
- **Auth**: `client_key` OR `basic_auth` OR `api_key_auth`
- **Server**: `default13`
- **Signature**: `def post_validate_bank_account_identification(*, body: BankAccountIdentificationValidationRequest | BankAccountIdentificationValidationRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, PostValidateBankAccountIdentificationErrorBody]`
- **Error**: `PostValidateBankAccountIdentificationErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `BankAccountIdentificationValidationRequest` | `adyen/models/bank_account_identification_validation_request.py` |
| `BankAccountIdentificationValidationRequestDict` | `adyen/models/bank_account_identification_validation_request.py` |
| `PostValidateBankAccountIdentificationErrorBody` | `adyen/errors/post_validate_bank_account_identification_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

