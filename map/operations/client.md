<!-- Generated file — do not edit; regenerated with the SDK. -->

# Client — operations

Accessor: `client` · Source: `adyen/client.py` · 18 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.abort_request

- **Route**: `POST /abort`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default24`
- **Signature**: `def abort_request(*, body: AbortRequest | AbortRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `Any`
- **Returns (raw)**: `ApiResult[Any, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `AbortRequest` | `adyen/models/abort_request.py` |
| `AbortRequestDict` | `adyen/models/abort_request.py` |

### client.admin_request

- **Route**: `POST /admin`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default24`
- **Signature**: `def admin_request(*, body: AdminRequest | AdminRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `AdminResponse`
- **Returns (raw)**: `ApiResult[AdminResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `AdminRequest` | `adyen/models/admin_request.py` |
| `AdminRequestDict` | `adyen/models/admin_request.py` |
| `AdminResponse` | `adyen/models/admin_response.py` |

### client.balance_inquiry_request

- **Route**: `POST /balanceinquiry`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default24`
- **Signature**: `def balance_inquiry_request(*, body: BalanceInquiryRequest | BalanceInquiryRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `BalanceInquiryResponse`
- **Returns (raw)**: `ApiResult[BalanceInquiryResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `BalanceInquiryRequest` | `adyen/models/balance_inquiry_request.py` |
| `BalanceInquiryRequestDict` | `adyen/models/balance_inquiry_request.py` |
| `BalanceInquiryResponse` | `adyen/models/balance_inquiry_response.py` |

### client.card_acquisition_request

- **Route**: `POST /cardacquisition`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default24`
- **Signature**: `def card_acquisition_request(*, body: CardAcquisitionRequest | CardAcquisitionRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `CardAcquisitionResponse`
- **Returns (raw)**: `ApiResult[CardAcquisitionResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CardAcquisitionRequest` | `adyen/models/card_acquisition_request.py` |
| `CardAcquisitionRequestDict` | `adyen/models/card_acquisition_request.py` |
| `CardAcquisitionResponse` | `adyen/models/card_acquisition_response.py` |

### client.card_reader_apdu_request

- **Route**: `POST /cardreaderapdu`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default24`
- **Signature**: `def card_reader_apdu_request(*, body: CardReaderApdurequest | CardReaderApdurequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `CardReaderApduresponse`
- **Returns (raw)**: `ApiResult[CardReaderApduresponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CardReaderApdurequest` | `adyen/models/card_reader_apdurequest.py` |
| `CardReaderApdurequestDict` | `adyen/models/card_reader_apdurequest.py` |
| `CardReaderApduresponse` | `adyen/models/card_reader_apduresponse.py` |

### client.diagnosis_request

- **Route**: `POST /diagnosis`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default24`
- **Signature**: `def diagnosis_request(*, body: DiagnosisRequest | DiagnosisRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `DiagnosisResponse`
- **Returns (raw)**: `ApiResult[DiagnosisResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `DiagnosisRequest` | `adyen/models/diagnosis_request.py` |
| `DiagnosisRequestDict` | `adyen/models/diagnosis_request.py` |
| `DiagnosisResponse` | `adyen/models/diagnosis_response.py` |

### client.display_request

- **Route**: `POST /display`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default24`
- **Signature**: `def display_request(*, body: DisplayRequest | DisplayRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `DisplayResponse`
- **Returns (raw)**: `ApiResult[DisplayResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `DisplayRequest` | `adyen/models/display_request.py` |
| `DisplayRequestDict` | `adyen/models/display_request.py` |
| `DisplayResponse` | `adyen/models/display_response.py` |

### client.enable_service_request

- **Route**: `POST /enableservice`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default24`
- **Signature**: `def enable_service_request(*, body: EnableServiceRequest | EnableServiceRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `EnableServiceResponse`
- **Returns (raw)**: `ApiResult[EnableServiceResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `EnableServiceRequest` | `adyen/models/enable_service_request.py` |
| `EnableServiceRequestDict` | `adyen/models/enable_service_request.py` |
| `EnableServiceResponse` | `adyen/models/enable_service_response.py` |

### client.get_totals_request

- **Route**: `POST /gettotals`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default24`
- **Signature**: `def get_totals_request(*, body: GetTotalsRequest | GetTotalsRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `GetTotalsResponse`
- **Returns (raw)**: `ApiResult[GetTotalsResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `GetTotalsRequest` | `adyen/models/get_totals_request.py` |
| `GetTotalsRequestDict` | `adyen/models/get_totals_request.py` |
| `GetTotalsResponse` | `adyen/models/get_totals_response.py` |

### client.input_request

- **Route**: `POST /input`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default24`
- **Signature**: `def input_request(*, body: InputRequest | InputRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `InputResponse`
- **Returns (raw)**: `ApiResult[InputResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `InputRequest` | `adyen/models/input_request.py` |
| `InputRequestDict` | `adyen/models/input_request.py` |
| `InputResponse` | `adyen/models/input_response.py` |

### client.login_request

- **Route**: `POST /login`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default24`
- **Signature**: `def login_request(*, body: LoginRequest | LoginRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `LoginResponse`
- **Returns (raw)**: `ApiResult[LoginResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `LoginRequest` | `adyen/models/login_request.py` |
| `LoginRequestDict` | `adyen/models/login_request.py` |
| `LoginResponse` | `adyen/models/login_response.py` |

### client.logout_request

- **Route**: `POST /logout`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default24`
- **Signature**: `def logout_request(*, body: LogoutRequest | LogoutRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `LogoutResponse`
- **Returns (raw)**: `ApiResult[LogoutResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `LogoutRequest` | `adyen/models/logout_request.py` |
| `LogoutRequestDict` | `adyen/models/logout_request.py` |
| `LogoutResponse` | `adyen/models/logout_response.py` |

### client.payment_request

- **Route**: `POST /payment`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default24`
- **Signature**: `def payment_request(*, body: PaymentRequest2 | PaymentRequest2Dict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `PaymentResponse4`
- **Returns (raw)**: `ApiResult[PaymentResponse4, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `PaymentRequest2` | `adyen/models/payment_request2.py` |
| `PaymentRequest2Dict` | `adyen/models/payment_request2.py` |
| `PaymentResponse4` | `adyen/models/payment_response4.py` |

### client.print_request

- **Route**: `POST /print`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default24`
- **Signature**: `def print_request(*, body: PrintRequest | PrintRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `PrintResponse`
- **Returns (raw)**: `ApiResult[PrintResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `PrintRequest` | `adyen/models/print_request.py` |
| `PrintRequestDict` | `adyen/models/print_request.py` |
| `PrintResponse` | `adyen/models/print_response.py` |

### client.reconciliation_request

- **Route**: `POST /reconciliation`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default24`
- **Signature**: `def reconciliation_request(*, body: ReconciliationRequest | ReconciliationRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `ReconciliationResponse`
- **Returns (raw)**: `ApiResult[ReconciliationResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ReconciliationRequest` | `adyen/models/reconciliation_request.py` |
| `ReconciliationRequestDict` | `adyen/models/reconciliation_request.py` |
| `ReconciliationResponse` | `adyen/models/reconciliation_response.py` |

### client.reversal_request

- **Route**: `POST /reversal`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default24`
- **Signature**: `def reversal_request(*, body: ReversalRequest | ReversalRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `ReversalResponse`
- **Returns (raw)**: `ApiResult[ReversalResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ReversalRequest` | `adyen/models/reversal_request.py` |
| `ReversalRequestDict` | `adyen/models/reversal_request.py` |
| `ReversalResponse` | `adyen/models/reversal_response.py` |

### client.stored_value_request

- **Route**: `POST /storedvalue`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default24`
- **Signature**: `def stored_value_request(*, body: StoredValueRequest | StoredValueRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `StoredValueResponse`
- **Returns (raw)**: `ApiResult[StoredValueResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `StoredValueRequest` | `adyen/models/stored_value_request.py` |
| `StoredValueRequestDict` | `adyen/models/stored_value_request.py` |
| `StoredValueResponse` | `adyen/models/stored_value_response.py` |

### client.transaction_status_request

- **Route**: `POST /transactionstatus`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default24`
- **Signature**: `def transaction_status_request(*, body: TransactionStatusRequest | TransactionStatusRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `TransactionStatusResponse`
- **Returns (raw)**: `ApiResult[TransactionStatusResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TransactionStatusRequest` | `adyen/models/transaction_status_request.py` |
| `TransactionStatusRequestDict` | `adyen/models/transaction_status_request.py` |
| `TransactionStatusResponse` | `adyen/models/transaction_status_response.py` |

