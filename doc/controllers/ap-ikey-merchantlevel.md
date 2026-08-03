# AP Ikey-Merchantlevel

```python
ap_ikey_merchantlevel_api = client.ap_ikey_merchantlevel
```

## Class Name

`ApIkeyMerchantlevelApi`


# Post-Merchants-Merchant Id-Api Credentials-Api Credential Id-Generate Api Key

Returns a new API key for the API credential. You can use the new API key a few minutes after generating it. The old API key stops working 24 hours after generating a new one.

To make this request, your API credential must have the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions):

* Management API—API credentials read and write

```python
def post_merchants_merchant_id_api_credentials_api_credential_id_generate_api_key(self,
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

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`GenerateApiKeyResponse`](../../doc/models/generate-api-key-response.md).

## Example Usage

```python
merchant_id = 'merchantId6'

api_credential_id = 'apiCredentialId8'

result = api_key_merchant_level_api.post_merchants_merchant_id_api_credentials_api_credential_id_generate_api_key(
    merchant_id,
    api_credential_id
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

