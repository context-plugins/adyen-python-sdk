# Allowedorigins-Merchantlevel

```python
allowedorigins_merchantlevel_api = client.allowedorigins_merchantlevel
```

## Class Name

`AllowedoriginsMerchantlevelApi`

## Methods

* [Get-Merchants-Merchant Id-Api Credentials-Api Credential Id-Allowed Origins](../../doc/controllers/allowedorigins-merchantlevel.md#get-merchants-merchant-id-api-credentials-api-credential-id-allowed-origins)
* [Post-Merchants-Merchant Id-Api Credentials-Api Credential Id-Allowed Origins](../../doc/controllers/allowedorigins-merchantlevel.md#post-merchants-merchant-id-api-credentials-api-credential-id-allowed-origins)
* [Get-Merchants-Merchant Id-Api Credentials-Api Credential Id-Allowed Origins-Origin Id](../../doc/controllers/allowedorigins-merchantlevel.md#get-merchants-merchant-id-api-credentials-api-credential-id-allowed-origins-origin-id)
* [Delete-Merchants-Merchant Id-Api Credentials-Api Credential Id-Allowed Origins-Origin Id](../../doc/controllers/allowedorigins-merchantlevel.md#delete-merchants-merchant-id-api-credentials-api-credential-id-allowed-origins-origin-id)


# Get-Merchants-Merchant Id-Api Credentials-Api Credential Id-Allowed Origins

Returns the list of [allowed origins](https://docs.adyen.com/development-resources/client-side-authentication#allowed-origins) for the API credential identified in the path.

To make this request, your API credential must have the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions):

* Management API—API credentials read and write

```python
def get_merchants_merchant_id_api_credentials_api_credential_id_allowed_origins(self,
                                                                               merchant_id,
                                                                               api_credential_id)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `merchant_id` | `str` | Template, Required | The unique identifier of the merchant account. |
| `api_credential_id` | `str` | Template, Required | Unique identifier of the API credential. |

## Response Type

**200**: OK - the request has succeeded.

[`AllowedOriginsResponse`](../../doc/models/allowed-origins-response.md)

## Example Usage

```python
merchant_id = 'merchantId6'

api_credential_id = 'apiCredentialId8'

result = allowed_origins_merchant_level_api.get_merchants_merchant_id_api_credentials_api_credential_id_allowed_origins(
    merchant_id,
    api_credential_id
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "data": [
    {
      "id": "YOUR_ALLOWED_ORIGIN_1",
      "domain": "https://www.eu.mystore.com",
      "_links": {
        "self": {
          "href": "https://management-test.adyen.com/v1/merchants/YOUR_MERCHANT_ACCOUNT/apiCredentials/YOUR_API_CREDENTIAL/allowedOrigins/YOUR_ALLOWED_ORIGIN_1"
        }
      }
    },
    {
      "id": "YOUR_ALLOWED_ORIGIN_2",
      "domain": "https://www.us.mystore.com",
      "_links": {
        "self": {
          "href": "https://management-test.adyen.com/v1/merchants/YOUR_MERCHANT_ACCOUNT/apiCredentials/YOUR_API_CREDENTIAL/allowedOrigins/YOUR_ALLOWED_ORIGIN_2"
        }
      }
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - a problem reading or understanding the request. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 401 | Unauthorized - authentication required. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |


# Post-Merchants-Merchant Id-Api Credentials-Api Credential Id-Allowed Origins

Adds a new [allowed origin](https://docs.adyen.com/development-resources/client-side-authentication#allowed-origins) to the API credential's list of allowed origins.

To make this request, your API credential must have the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions):

* Management API—API credentials read and write

```python
def post_merchants_merchant_id_api_credentials_api_credential_id_allowed_origins(self,
                                                                                merchant_id,
                                                                                api_credential_id,
                                                                                body=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `merchant_id` | `str` | Template, Required | The unique identifier of the merchant account. |
| `api_credential_id` | `str` | Template, Required | Unique identifier of the API credential. |
| `body` | [`AllowedOrigin`](../../doc/models/allowed-origin.md) | Body, Optional | - |

## Response Type

**200**: OK - the request has succeeded.

[`AllowedOrigin`](../../doc/models/allowed-origin.md)

## Example Usage

```python
merchant_id = 'merchantId6'

api_credential_id = 'apiCredentialId8'

body = AllowedOrigin(
    domain='https://www.eu.mystore.com'
)

result = allowed_origins_merchant_level_api.post_merchants_merchant_id_api_credentials_api_credential_id_allowed_origins(
    merchant_id,
    api_credential_id,
    body=body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "domain": "https://www.eu.mystore.com",
  "_links": {
    "self": {
      "href": "https://management-test.adyen.com/v1/merchants/YOUR_MERCHANT_ACCOUNT/apiCredentials/YOUR_API_CREDENTIAL/allowedOrigins/YOUR_ALLOWED_ORIGIN"
    }
  }
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - a problem reading or understanding the request. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 401 | Unauthorized - authentication required. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |


# Get-Merchants-Merchant Id-Api Credentials-Api Credential Id-Allowed Origins-Origin Id

Returns the [allowed origin](https://docs.adyen.com/development-resources/client-side-authentication#allowed-origins) identified in the path.

To make this request, your API credential must have the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions):

* Management API—API credentials read and write

```python
def get_merchants_merchant_id_api_credentials_api_credential_id_allowed_origins_origin_id(self,
                                                                                         merchant_id,
                                                                                         api_credential_id,
                                                                                         origin_id)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `merchant_id` | `str` | Template, Required | The unique identifier of the merchant account. |
| `api_credential_id` | `str` | Template, Required | Unique identifier of the API credential. |
| `origin_id` | `str` | Template, Required | Unique identifier of the allowed origin. |

## Response Type

**200**: OK - the request has succeeded.

[`AllowedOrigin`](../../doc/models/allowed-origin.md)

## Example Usage

```python
merchant_id = 'merchantId6'

api_credential_id = 'apiCredentialId8'

origin_id = 'originId6'

result = allowed_origins_merchant_level_api.get_merchants_merchant_id_api_credentials_api_credential_id_allowed_origins_origin_id(
    merchant_id,
    api_credential_id,
    origin_id
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "id": "YOUR_ALLOWED_ORIGIN",
  "domain": "https://www.eu.mystore.com",
  "_links": {
    "self": {
      "href": "https://management-test.adyen.com/v1/merchants/YOUR_MERCHANT_ACCOUNT/apiCredentials/YOUR_API_CREDENTIAL/allowedOrigins/YOUR_ALLOWED_ORIGIN"
    }
  }
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - a problem reading or understanding the request. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 401 | Unauthorized - authentication required. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |


# Delete-Merchants-Merchant Id-Api Credentials-Api Credential Id-Allowed Origins-Origin Id

Removes the [allowed origin](https://docs.adyen.com/development-resources/client-side-authentication#allowed-origins) identified in the path. As soon as an allowed origin is removed, we no longer accept client-side requests from that domain.

To make this request, your API credential must have the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions):

* Management API—API credentials read and write

```python
def delete_merchants_merchant_id_api_credentials_api_credential_id_allowed_origins_origin_id(self,
                                                                                            merchant_id,
                                                                                            api_credential_id,
                                                                                            origin_id)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `merchant_id` | `str` | Template, Required | The unique identifier of the merchant account. |
| `api_credential_id` | `str` | Template, Required | Unique identifier of the API credential. |
| `origin_id` | `str` | Template, Required | Unique identifier of the allowed origin. |

## Response Type

**204**: No Content - look at the actual response code for the status of the request.

`void`

## Example Usage

```python
merchant_id = 'merchantId6'

api_credential_id = 'apiCredentialId8'

origin_id = 'originId6'

allowed_origins_merchant_level_api.delete_merchants_merchant_id_api_credentials_api_credential_id_allowed_origins_origin_id(
    merchant_id,
    api_credential_id,
    origin_id
)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - a problem reading or understanding the request. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 401 | Unauthorized - authentication required. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |

