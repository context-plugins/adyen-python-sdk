# Sessionauthentication

```python
sessionauthentication_api = client.sessionauthentication
```

## Class Name

`SessionauthenticationApi`

## Methods

* [Post-Sessions](../../doc/controllers/sessionauthentication.md#post-sessions)
* [Post-Auth-Certificate](../../doc/controllers/sessionauthentication.md#post-auth-certificate)


# Post-Sessions

Creates a session token that is required to integrate [components](https://docs.adyen.com/platforms/components-overview).

The response contains encrypted session data. The front end then uses the session data to make the required server-side calls for the component.

To create a token, you must meet specific requirements. These requirements vary depending on the type of component. For more information, see the documentation for [Onboarding](https://docs.adyen.com/platforms/onboard-users/components) and [Platform Experience](https://docs.adyen.com/platforms/build-user-dashboards) components.

:information_source: **Note** This endpoint does not require authentication.

```python
def post_sessions(self,
                 body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`AuthenticationSessionRequest`](../../doc/models/authentication-session-request.md) | Body, Required | - |

## Response Type

**200**: Successful operation

[`AuthenticationSessionResponse`](../../doc/models/authentication-session-response.md)

## Example Usage

```python
body = AuthenticationSessionRequest(
    allow_origin='https://www.your-website.com',
    policy=Policy2(
        resources=[
            LegalEntityResource(
                legal_entity_id='LE00000000000000000000001',
                mtype='legalEntity'
            )
        ],
        roles=[
            'createTransferInstrumentComponent',
            'manageTransferInstrumentComponent'
        ]
    ),
    product=ProductType2Enum.ONBOARDING
)

result = session_authentication_api.post_sessions(body)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "id": "11a1e60a-18b0-4dda-9258-e0ae29e1e2a3",
  "token": "eyJraWQiOiJwbGF0Zm9ybWNvbGRlciI..."
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |
| 401 | Unauthorized | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |
| 403 | Forbidden | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |


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

[`CertificateLoadingResponse`](../../doc/models/certificate-loading-response.md)

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
print(result)
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
| 400 | Bad request - validation failed. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |
| 401 | Unauthorized - authentication required. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |
| 422 | Unprocessable entity - session request could not be processed. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |
| 500 | Internal server error. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |

