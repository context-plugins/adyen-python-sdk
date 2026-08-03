# Hosted Onboarding Page

```python
hosted_onboarding_page_api = client.hosted_onboarding_page
```

## Class Name

`HostedOnboardingPageApi`


# Post-Get Onboarding Url

Returns a link to an Adyen-hosted onboarding page (HOP) that you can send to your account holder. For more information on how to use HOP, refer to [Hosted onboarding](https://docs.adyen.com/classic-platforms/onboard-users/hosted-onboarding-page).

```python
def post_get_onboarding_url(self,
                           body=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`GetOnboardingUrlRequest`](../../doc/models/get-onboarding-url-request.md) | Body, Optional | - |

## Response Type

**200**: OK - the request has succeeded.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`GetOnboardingUrlResponse`](../../doc/models/get-onboarding-url-response.md).

## Example Usage

```python
body = GetOnboardingUrlRequest(
    account_holder_code='CODE_OF_ACCOUNT_HOLDER',
    return_url='https://your.return-url.com/?submerchant=123'
)

result = hosted_onboarding_page_api.post_get_onboarding_url(
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
  "invalidFields": [],
  "pspReference": "9115677600500127",
  "resultCode": "Success",
  "redirectUrl": "https://hop-test.adyen.com/hop/view/?token=<token>"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - a problem reading or understanding the request. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |
| 401 | Unauthorized - authentication required. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |

