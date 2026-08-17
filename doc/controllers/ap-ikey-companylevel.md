# AP Ikey-Companylevel

```python
ap_ikey_companylevel_api = client.ap_ikey_companylevel
```

## Class Name

`APIkeyCompanylevelApi`


# Post-Companies-Company Id-Api Credentials-Api Credential Id-Generate Api Key

Returns a new API key for the API credential. You can use the new API key a few minutes after generating it. The old API key stops working 24 hours after generating a new one.

To make this request, your API credential must have the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions):

* Management API—API credentials read and write

```python
def post_companies_company_id_api_credentials_api_credential_id_generate_api_key(self,
                                                                                company_id,
                                                                                api_credential_id)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `company_id` | `str` | Template, Required | The unique identifier of the company account. |
| `api_credential_id` | `str` | Template, Required | Unique identifier of the API credential. |

## Response Type

**200**: OK - the request has succeeded.

[`GenerateApiKeyResponse`](../../doc/models/generate-api-key-response.md)

## Example Usage

```python
company_id = 'companyId0'

api_credential_id = 'apiCredentialId8'

result = api_key_company_level_api.post_companies_company_id_api_credentials_api_credential_id_generate_api_key(
    company_id,
    api_credential_id
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - a problem reading or understanding the request. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 401 | Unauthorized - authentication required. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |

