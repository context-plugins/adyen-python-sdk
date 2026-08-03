# Clientkey-Merchantlevel

```python
clientkey_merchantlevel_api = client.clientkey_merchantlevel
```

## Class Name

`ClientkeyMerchantlevelApi`


# Post-Merchants-Merchant Id-Api Credentials-Api Credential Id-Generate Client Key

Returns a new [client key](https://docs.adyen.com/development-resources/client-side-authentication#how-it-works) for the API credential identified in the path. You can use the new client key a few minutes after generating it. The old client key stops working 24 hours after generating a new one.

To make this request, your API credential must have the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions):

* Management API—API credentials read and write

```python
def post_merchants_merchant_id_api_credentials_api_credential_id_generate_client_key(self,
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

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`GenerateClientKeyResponse`](../../doc/models/generate-client-key-response.md).

## Example Usage

```python
merchant_id = 'merchantId6'

api_credential_id = 'apiCredentialId8'

result = client_key_merchant_level_api.post_merchants_merchant_id_api_credentials_api_credential_id_generate_client_key(
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

