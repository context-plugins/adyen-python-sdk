<!-- Generated file — do not edit; regenerated with the SDK. -->

# PaymentMethodsMerchantLevel — operations

Accessor: `client.payment_methods_merchant_level` · Source: `adyen/apis/payment_methods_merchant_level.py` · 6 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.payment_methods_merchant_level.get_merchants_merchant_id_payment_method_settings

- **Route**: `GET /merchants/{merchantId}/paymentMethodSettings`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default9`
- **Signature**: `def get_merchants_merchant_id_payment_method_settings(merchant_id: str, *, store_id: str | None = None, business_line_id: str | None = None, page_size: int | None = None, page_number: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `merchant_id`
- **Params**: `merchant_id` — path `merchantId` · `store_id` — query `storeId` · `business_line_id` — query `businessLineId` · `page_size` — query `pageSize` · `page_number` — query `pageNumber`
- **Returns (parsed)**: `PaymentMethodResponse`
- **Returns (raw)**: `ApiResult[PaymentMethodResponse, GetMerchantsMerchantIdPaymentMethodSettingsErrorBody]`
- **Error**: `GetMerchantsMerchantIdPaymentMethodSettingsErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `PaymentMethodResponse` | `adyen/models/payment_method_response.py` |
| `GetMerchantsMerchantIdPaymentMethodSettingsErrorBody` | `adyen/errors/get_merchants_merchant_id_payment_method_settings_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.payment_methods_merchant_level.get_merchants_merchant_id_payment_method_settings_payment_method_id

- **Route**: `GET /merchants/{merchantId}/paymentMethodSettings/{paymentMethodId}`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default9`
- **Signature**: `def get_merchants_merchant_id_payment_method_settings_payment_method_id(merchant_id: str, payment_method_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `merchant_id`, `payment_method_id`
- **Params**: `merchant_id` — path `merchantId` · `payment_method_id` — path `paymentMethodId`
- **Returns (parsed)**: `ManagementPaymentMethod`
- **Returns (raw)**: `ApiResult[ManagementPaymentMethod, GetMerchantsMerchantIdPaymentMethodSettingsPaymentMethodIdErrorBody]`
- **Error**: `GetMerchantsMerchantIdPaymentMethodSettingsPaymentMethodIdErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ManagementPaymentMethod` | `adyen/models/management_payment_method.py` |
| `GetMerchantsMerchantIdPaymentMethodSettingsPaymentMethodIdErrorBody` | `adyen/errors/get_merchants_merchant_id_payment_method_settings_payment_method_id_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.payment_methods_merchant_level.get_merchants_merchant_id_payment_method_settings_payment_method_id_get_apple_pay_domains

- **Route**: `GET /merchants/{merchantId}/paymentMethodSettings/{paymentMethodId}/getApplePayDomains`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default9`
- **Signature**: `def get_merchants_merchant_id_payment_method_settings_payment_method_id_get_apple_pay_domains(merchant_id: str, payment_method_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `merchant_id`, `payment_method_id`
- **Params**: `merchant_id` — path `merchantId` · `payment_method_id` — path `paymentMethodId`
- **Returns (parsed)**: `ApplePayResponseInfo`
- **Returns (raw)**: `ApiResult[ApplePayResponseInfo, GetMerchantsMerchantIdPaymentMethodSettingsPaymentMethodIdGetApplePayDomainsErrorBody]`
- **Error**: `GetMerchantsMerchantIdPaymentMethodSettingsPaymentMethodIdGetApplePayDomainsErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ApplePayResponseInfo` | `adyen/models/apple_pay_response_info.py` |
| `GetMerchantsMerchantIdPaymentMethodSettingsPaymentMethodIdGetApplePayDomainsErrorBody` | `adyen/errors/get_merchants_merchant_id_payment_method_settings_payment_method_id_get_apple_pay_domains_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.payment_methods_merchant_level.patch_merchants_merchant_id_payment_method_settings_payment_method_id

- **Route**: `PATCH /merchants/{merchantId}/paymentMethodSettings/{paymentMethodId}`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default9`
- **Signature**: `def patch_merchants_merchant_id_payment_method_settings_payment_method_id(merchant_id: str, payment_method_id: str, *, body: UpdatePaymentMethodInfo | UpdatePaymentMethodInfoDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `merchant_id`, `payment_method_id`
- **Params**: `merchant_id` — path `merchantId` · `payment_method_id` — path `paymentMethodId` · `body` — JSON body
- **Returns (parsed)**: `ManagementPaymentMethod`
- **Returns (raw)**: `ApiResult[ManagementPaymentMethod, PatchMerchantsMerchantIdPaymentMethodSettingsPaymentMethodIdErrorBody]`
- **Error**: `PatchMerchantsMerchantIdPaymentMethodSettingsPaymentMethodIdErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `UpdatePaymentMethodInfo` | `adyen/models/update_payment_method_info.py` |
| `UpdatePaymentMethodInfoDict` | `adyen/models/update_payment_method_info.py` |
| `ManagementPaymentMethod` | `adyen/models/management_payment_method.py` |
| `PatchMerchantsMerchantIdPaymentMethodSettingsPaymentMethodIdErrorBody` | `adyen/errors/patch_merchants_merchant_id_payment_method_settings_payment_method_id_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.payment_methods_merchant_level.post_merchants_merchant_id_payment_method_settings

- **Route**: `POST /merchants/{merchantId}/paymentMethodSettings`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default9`
- **Signature**: `def post_merchants_merchant_id_payment_method_settings(merchant_id: str, *, body: PaymentMethodSetupInfo | PaymentMethodSetupInfoDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `merchant_id`
- **Params**: `merchant_id` — path `merchantId` · `body` — JSON body
- **Returns (parsed)**: `ManagementPaymentMethod`
- **Returns (raw)**: `ApiResult[ManagementPaymentMethod, PostMerchantsMerchantIdPaymentMethodSettingsErrorBody]`
- **Error**: `PostMerchantsMerchantIdPaymentMethodSettingsErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `PaymentMethodSetupInfo` | `adyen/models/payment_method_setup_info.py` |
| `PaymentMethodSetupInfoDict` | `adyen/models/payment_method_setup_info.py` |
| `ManagementPaymentMethod` | `adyen/models/management_payment_method.py` |
| `PostMerchantsMerchantIdPaymentMethodSettingsErrorBody` | `adyen/errors/post_merchants_merchant_id_payment_method_settings_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.payment_methods_merchant_level.post_merchants_merchant_id_payment_method_settings_payment_method_id_add_apple_pay_domains

- **Route**: `POST /merchants/{merchantId}/paymentMethodSettings/{paymentMethodId}/addApplePayDomains`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default9`
- **Signature**: `def post_merchants_merchant_id_payment_method_settings_payment_method_id_add_apple_pay_domains(merchant_id: str, payment_method_id: str, *, body: ApplePayInfo | ApplePayInfoDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `merchant_id`, `payment_method_id`
- **Params**: `merchant_id` — path `merchantId` · `payment_method_id` — path `paymentMethodId` · `body` — JSON body
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, PostMerchantsMerchantIdPaymentMethodSettingsPaymentMethodIdAddApplePayDomainsErrorBody]`
- **Error**: `PostMerchantsMerchantIdPaymentMethodSettingsPaymentMethodIdAddApplePayDomainsErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ApplePayInfo` | `adyen/models/apple_pay_info.py` |
| `ApplePayInfoDict` | `adyen/models/apple_pay_info.py` |
| `PostMerchantsMerchantIdPaymentMethodSettingsPaymentMethodIdAddApplePayDomainsErrorBody` | `adyen/errors/post_merchants_merchant_id_payment_method_settings_payment_method_id_add_apple_pay_domains_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

