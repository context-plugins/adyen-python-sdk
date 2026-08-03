# Hosted Onboarding

```python
hosted_onboarding_api = client.hosted_onboarding
```

## Class Name

`HostedOnboardingApi`

## Methods

* [Post-Legal Entities-Id-Onboarding Links](../../doc/controllers/hosted-onboarding.md#post-legal-entities-id-onboarding-links)
* [Get-Themes](../../doc/controllers/hosted-onboarding.md#get-themes)
* [Get-Themes-Id](../../doc/controllers/hosted-onboarding.md#get-themes-id)


# Post-Legal Entities-Id-Onboarding Links

Returns a link to an Adyen-hosted onboarding page where you need to redirect your user.

Requests to this endpoint are subject to rate limits:

- Live environments: 700 requests per 5 seconds.

- Test environments: 200 requests per 5 seconds.

- Failed requests are subject to a limit of 5 failures per 10 seconds.

```python
def post_legal_entities_id_onboarding_links(self,
                                           id,
                                           body=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The unique identifier of the legal entity |
| `body` | [`OnboardingLinkInfo`](../../doc/models/onboarding-link-info.md) | Body, Optional | - |

## Response Type

**200**: OK - the request has succeeded.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`OnboardingLink`](../../doc/models/onboarding-link.md).

## Example Usage

```python
id = 'id0'

body = OnboardingLinkInfo(
    locale='nl-NL',
    redirect_url='https://your-company.example.com',
    theme_id='YOUR_THEME_ID'
)

result = hosted_onboarding_api.post_legal_entities_id_onboarding_links(
    id,
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
  "url": "https://balanceplatform-test.adyen.com/balanceplatform/uo/form/xtl-...?signature=..&cd=..&redirectUrl=https%3A%2F%2Fyour-company.example.com%2F&expiry=1667226404807&locale=nl-NL"
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


# Get-Themes

Returns a list of hosted onboarding page themes.

Requests to this endpoint are subject to rate limits:

- Live environments: 700 requests per 5 seconds.

- Test environments: 200 requests per 5 seconds.

- Failed requests are subject to a limit of 5 failures per 10 seconds.

```python
def get_themes(self)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Response Type

**200**: OK - the request has succeeded.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`OnboardingThemes`](../../doc/models/onboarding-themes.md).

## Example Usage

```python
result = hosted_onboarding_api.get_themes()

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "themes": [
    {
      "description": "Dark colors theme",
      "properties": {
        "supportPage": "https://www.adyen.com/contact",
        "logo": "ONBA422JV223222D5G8VG2T8JV39GV",
        "pageTitle": "Example onboarding dark colors",
        "backgroundColor": "#000000",
        "faqPage": "https://docs.adyen.com/hosted-onboarding-faqs",
        "backgroundImage": "ONBA422KH223222D5G8VG2TG9S5ZBH",
        "pageLayout": "withBackground"
      },
      "createdAt": "2022-01-20T00:00:00+01:00",
      "id": "ONBT422JV223222D5FGJ77B9C52WNN",
      "updatedAt": "2022-08-25T00:00:00+02:00"
    },
    {
      "description": "Light colors theme",
      "properties": {
        "privacyStatementPage": "https://www.adyen.com/legal/terms-and-conditions",
        "supportPage": "https://www.adyen.com/contact",
        "logo": "ONBA422JV223222D5FWC4TK25S3DQW",
        "pageTitle": "Example onboarding light colors",
        "backgroundColor": "#FFFFFF",
        "faqPage": "https://docs.adyen.com/hosted-onboarding-faqs",
        "backgroundImage": "ONBA422JV223222D5G82M96F6P2VTV",
        "pageLayout": "withBackground"
      },
      "createdAt": "2022-06-22T00:00:00+02:00",
      "id": "ONBT422KH223222D5G82M968PB46HR",
      "updatedAt": "2022-08-25T00:00:00+02:00"
    }
  ]
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


# Get-Themes-Id

Returns the details of the theme identified in the path.

Requests to this endpoint are subject to rate limits:

- Live environments: 700 requests per 5 seconds.

- Test environments: 200 requests per 5 seconds.

- Failed requests are subject to a limit of 5 failures per 10 seconds.

```python
def get_themes_id(self,
                 id)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The unique identifier of the theme |

## Response Type

**200**: OK - the request has succeeded.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`OnboardingTheme`](../../doc/models/onboarding-theme.md).

## Example Usage

```python
id = 'id0'

result = hosted_onboarding_api.get_themes_id(id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "description": "Light colors theme",
  "properties": {
    "privacyStatementPage": "https://www.adyen.com/legal/terms-and-conditions",
    "supportPage": "https://www.adyen.com/contact",
    "logo": "ONBA422JV223222D5FWC4TK25S3DQW",
    "pageTitle": "Example onboarding light colors",
    "backgroundColor": "#FFFFFF",
    "faqPage": "https://docs.adyen.com/hosted-onboarding-faqs",
    "backgroundImage": "ONBA422JV223222D5G82M96F6P2VTV",
    "pageLayout": "withBackground"
  },
  "createdAt": "2022-06-22T00:00:00+02:00",
  "id": "ONBT422KH223222D5G82M968PB46HR",
  "updatedAt": "2022-08-25T00:00:00+02:00"
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

