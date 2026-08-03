# Sessionauthentication

```python
sessionauthentication_api = client.sessionauthentication
```

## Class Name

`SessionauthenticationApi`


# Post-Auth-Certificate

Establishes a secure communication session between the Mobile SDK and the Adyen payments platform, through mutual authentication. The request sends a setup token that identifies the SDK and the device. The response returns a session token that the SDK can use to authenticate responses received from the Adyen payments platform.

:information_source: **Note** This endpoint does not require authentication.

```python
def post_auth_certificate(self,
                         x_api_key=None,
                         body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `x_api_key` | `str` | Header, Optional | The API key to authenticate API requests. |
| `body` | [`CertificateLoadingRequest`](../../doc/models/certificate-loading-request.md) | Body, Optional | - |

## Response Type

**201**: OK - the request has succeeded.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`CreateSessionResponse`](../../doc/models/create-session-response.md).

## Example Usage

```python
body = CertificateLoadingRequest(
    merchant_account='YOUR_MERCHANT_ACCOUNT',
    setup_token='SETUP_TOKEN',
    store='YOUR_STORE_REFERENCE'
)

result = session_authentication_api.post_auth_certificate(
    body=body
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "id": "APP_SESSION_ID",
  "installationId": "INSTALLATION_ID",
  "merchantAccount": "YOUR_MERCHANT_ACCOUNT",
  "store": "YOUR_STORE_REFERENCE",
  "sdkData": "SDK_DATA_BLOB"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request - validation failed. | [`AuthCertificate400ErrorException`](../../doc/models/auth-certificate-400-error-exception.md) |
| 401 | Unauthorized - authentication required. | [`AuthCertificate401ErrorException`](../../doc/models/auth-certificate-401-error-exception.md) |
| 422 | Unprocessable entity - session request could not be processed. | [`AuthCertificate422ErrorException`](../../doc/models/auth-certificate-422-error-exception.md) |
| 500 | Internal server error. | [`AuthCertificate500ErrorException`](../../doc/models/auth-certificate-500-error-exception.md) |

