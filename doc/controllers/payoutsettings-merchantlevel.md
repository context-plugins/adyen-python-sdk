# Payoutsettings-Merchantlevel

```python
payoutsettings_merchantlevel_api = client.payoutsettings_merchantlevel
```

## Class Name

`PayoutsettingsMerchantlevelApi`

## Methods

* [Get-Merchants-Merchant Id-Payout Settings](../../doc/controllers/payoutsettings-merchantlevel.md#get-merchants-merchant-id-payout-settings)
* [Post-Merchants-Merchant Id-Payout Settings](../../doc/controllers/payoutsettings-merchantlevel.md#post-merchants-merchant-id-payout-settings)
* [Get-Merchants-Merchant Id-Payout Settings-Payout Settings Id](../../doc/controllers/payoutsettings-merchantlevel.md#get-merchants-merchant-id-payout-settings-payout-settings-id)
* [Delete-Merchants-Merchant Id-Payout Settings-Payout Settings Id](../../doc/controllers/payoutsettings-merchantlevel.md#delete-merchants-merchant-id-payout-settings-payout-settings-id)
* [Patch-Merchants-Merchant Id-Payout Settings-Payout Settings Id](../../doc/controllers/payoutsettings-merchantlevel.md#patch-merchants-merchant-id-payout-settings-payout-settings-id)


# Get-Merchants-Merchant Id-Payout Settings

Returns the list of payout settings for the merchant account identified in the path.

Use this endpoint if your integration requires it, such as Adyen for Platforms Manage. Your Adyen contact will set up your access.

To make this request, your API credential must have the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions):

* Management API—Payout account settings read

```python
def get_merchants_merchant_id_payout_settings(self,
                                             merchant_id)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `merchant_id` | `str` | Template, Required | The unique identifier of the merchant account. |

## Response Type

**200**: OK - the request has succeeded.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`PayoutSettingsResponse`](../../doc/models/payout-settings-response.md).

## Example Usage

```python
merchant_id = 'merchantId6'

result = payout_settings_merchant_level_api.get_merchants_merchant_id_payout_settings(merchant_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - a problem reading or understanding the request. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 401 | Unauthorized - authentication required. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |


# Post-Merchants-Merchant Id-Payout Settings

Sends a request to add a payout setting for the merchant account specified in the path. A payout setting links the merchant account to the [transfer instrument](https://docs.adyen.com/api-explorer/#/legalentity/latest/post/transferInstruments) that contains the details of the payout bank account. Adyen verifies the bank account before allowing and enabling the payout setting.

If you're accepting payments in multiple currencies, you may add multiple payout settings for the merchant account.

Use this endpoint if your integration requires it, such as Adyen for Platforms Manage. Your Adyen contact will set up your access.

To make this request, your API credential must have the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions):

* Management API—Payout account settings read and write

```python
def post_merchants_merchant_id_payout_settings(self,
                                              merchant_id,
                                              body=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `merchant_id` | `str` | Template, Required | The unique identifier of the merchant account. |
| `body` | [`PayoutSettingsRequest`](../../doc/models/payout-settings-request.md) | Body, Optional | - |

## Response Type

**200**: OK - the request has succeeded.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`PayoutSettings`](../../doc/models/payout-settings.md).

## Example Usage

```python
merchant_id = 'merchantId6'

result = payout_settings_merchant_level_api.post_merchants_merchant_id_payout_settings(merchant_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - a problem reading or understanding the request. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 401 | Unauthorized - authentication required. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |


# Get-Merchants-Merchant Id-Payout Settings-Payout Settings Id

Returns the payout setting identified in the path.

Use this endpoint if your integration requires it, such as Adyen for Platforms Manage. Your Adyen contact will set up your access.

To make this request, your API credential must have the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions):

* Management API—Payout account settings read

```python
def get_merchants_merchant_id_payout_settings_payout_settings_id(self,
                                                                merchant_id,
                                                                payout_settings_id)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `merchant_id` | `str` | Template, Required | The unique identifier of the merchant account. |
| `payout_settings_id` | `str` | Template, Required | The unique identifier of the payout setting. |

## Response Type

**200**: OK - the request has succeeded.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`PayoutSettings`](../../doc/models/payout-settings.md).

## Example Usage

```python
merchant_id = 'merchantId6'

payout_settings_id = 'payoutSettingsId6'

result = payout_settings_merchant_level_api.get_merchants_merchant_id_payout_settings_payout_settings_id(
    merchant_id,
    payout_settings_id
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - a problem reading or understanding the request. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 401 | Unauthorized - authentication required. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |


# Delete-Merchants-Merchant Id-Payout Settings-Payout Settings Id

Deletes the payout setting identified in the path.

Use this endpoint if your integration requires it, such as Adyen for Platforms Manage. Your Adyen contact will set up your access.

To make this request, your API credential must have the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions):

* Management API—Payout account settings read and write

```python
def delete_merchants_merchant_id_payout_settings_payout_settings_id(self,
                                                                   merchant_id,
                                                                   payout_settings_id)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `merchant_id` | `str` | Template, Required | The unique identifier of the merchant account. |
| `payout_settings_id` | `str` | Template, Required | The unique identifier of the payout setting. |

## Response Type

**204**: No Content - look at the actual response code for the status of the request.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance.

## Example Usage

```python
merchant_id = 'merchantId6'

payout_settings_id = 'payoutSettingsId6'

result = payout_settings_merchant_level_api.delete_merchants_merchant_id_payout_settings_payout_settings_id(
    merchant_id,
    payout_settings_id
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - a problem reading or understanding the request. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 401 | Unauthorized - authentication required. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |


# Patch-Merchants-Merchant Id-Payout Settings-Payout Settings Id

Updates the payout setting identified in the path. You can enable or disable the payout setting.

Use this endpoint if your integration requires it, such as Adyen for Platforms Manage. Your Adyen contact will set up your access.

To make this request, your API credential must have the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions):

* Management API—Payout account settings read and write

```python
def patch_merchants_merchant_id_payout_settings_payout_settings_id(self,
                                                                  merchant_id,
                                                                  payout_settings_id,
                                                                  body=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `merchant_id` | `str` | Template, Required | The unique identifier of the merchant account. |
| `payout_settings_id` | `str` | Template, Required | The unique identifier of the payout setting. |
| `body` | [`UpdatePayoutSettingsRequest`](../../doc/models/update-payout-settings-request.md) | Body, Optional | - |

## Response Type

**200**: OK - the request has succeeded.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`PayoutSettings`](../../doc/models/payout-settings.md).

## Example Usage

```python
merchant_id = 'merchantId6'

payout_settings_id = 'payoutSettingsId6'

result = payout_settings_merchant_level_api.patch_merchants_merchant_id_payout_settings_payout_settings_id(
    merchant_id,
    payout_settings_id
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - a problem reading or understanding the request. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 401 | Unauthorized - authentication required. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |

