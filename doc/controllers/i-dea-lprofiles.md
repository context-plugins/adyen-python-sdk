# I DEA Lprofiles

```python
i_dea_lprofiles_api = client.i_dea_lprofiles
```

## Class Name

`IdeaLprofilesApi`

## Methods

* [Post-Ideal-Profile-Auth-Link](../../doc/controllers/i-dea-lprofiles.md#post-ideal-profile-auth-link)
* [Post-Ideal-Profile-Authenticate](../../doc/controllers/i-dea-lprofiles.md#post-ideal-profile-authenticate)
* [Post-Ideal-Profile-Register](../../doc/controllers/i-dea-lprofiles.md#post-ideal-profile-register)


# Post-Ideal-Profile-Auth-Link

Manage an already registered iDEAL profile. Generates a redirection URL to manage the iDEAL profile linked to the account holder from the request.

:information_source: **Note** This endpoint does not require authentication.

```python
def post_ideal_profile_auth_link(self,
                                body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`IdealAuthLinkRequest`](../../doc/models/ideal-auth-link-request.md) | Body, Required | - |

## Response Type

**200**: OK - The request has succeeded.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`IdealAuthLinkResponse`](../../doc/models/ideal-auth-link-response.md).

## Example Usage

```python
body = IdealAuthLinkRequest(
    account_holder_id='AH00000000000000000000000'
)

result = i_deal_profiles_api.post_ideal_profile_auth_link(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "redirectUrl": {
    "href": "https://ideal.auth/someUrl"
  }
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - The request is malformed or is not the expected format. | [`IdealProfileAuthLink400ErrorException`](../../doc/models/ideal-profile-auth-link-400-error-exception.md) |
| 422 | Unprocessable Entity - A request validation error. | [`IdealProfileAuthLink422ErrorException`](../../doc/models/ideal-profile-auth-link-422-error-exception.md) |
| 500 | Internal Service Error - An unrecoverable error occurred while trying to perform the request. | [`IdealProfileAuthLink500ErrorException`](../../doc/models/ideal-profile-auth-link-500-error-exception.md) |


# Post-Ideal-Profile-Authenticate

Generates an redirection URL to finish the authentication flow when requested by iDEAL. Before calling this endpoint, make sure that your user has completed multi-factor authentication.

:information_source: **Note** This endpoint does not require authentication.

```python
def post_ideal_profile_authenticate(self,
                                   body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`IdealAuthenticateRequest`](../../doc/models/ideal-authenticate-request.md) | Body, Required | - |

## Response Type

**200**: OK - The request has succeeded.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`IdealAuthLinkResponse`](../../doc/models/ideal-auth-link-response.md).

## Example Usage

```python
body = IdealAuthenticateRequest(
    account_holder_id='AH00000000000000000000000',
    payload='https://ideal.auth/somePayload'
)

result = i_deal_profiles_api.post_ideal_profile_authenticate(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "redirectUrl": {
    "href": "https://ideal.auth/someUrl"
  }
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - The request is malformed or is not the expected format. | [`IdealProfileAuthenticate400ErrorException`](../../doc/models/ideal-profile-authenticate-400-error-exception.md) |
| 422 | Unprocessable Entity - A request validation error. | [`IdealProfileAuthenticate422ErrorException`](../../doc/models/ideal-profile-authenticate-422-error-exception.md) |
| 500 | Internal Service Error - An unrecoverable error occurred while trying to perform the request. | [`IdealProfileAuthenticate500ErrorException`](../../doc/models/ideal-profile-authenticate-500-error-exception.md) |


# Post-Ideal-Profile-Register

Register a new iDEAL profile. The profile is linked to the account holder and payment instruments included in the request. The user must be redirected to the URL in the response to finish their IDEAL profile registration.

:information_source: **Note** This endpoint does not require authentication.

```python
def post_ideal_profile_register(self,
                               body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`ProfileRegistrationRequest`](../../doc/models/profile-registration-request.md) | Body, Required | - |

## Response Type

**200**: OK - The request has succeeded.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`IdealAuthLinkResponse`](../../doc/models/ideal-auth-link-response.md).

## Example Usage

```python
body = ProfileRegistrationRequest(
    account_holder_id='AH00000000000000000000000',
    payment_instrument_ids=[
        'PI00000000000000000000000',
        'PI11111111111111111111111'
    ]
)

result = i_deal_profiles_api.post_ideal_profile_register(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "redirectUrl": {
    "href": "https://ideal.auth/someUrl"
  }
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - The request is malformed or is not the expected format. | [`IdealProfileRegister400ErrorException`](../../doc/models/ideal-profile-register-400-error-exception.md) |
| 422 | Unprocessable Entity - A request validation error. | [`IdealProfileRegister422ErrorException`](../../doc/models/ideal-profile-register-422-error-exception.md) |
| 500 | Internal Service Error - An unrecoverable error occurred while trying to perform the request. | [`IdealProfileRegister500ErrorException`](../../doc/models/ideal-profile-register-500-error-exception.md) |

