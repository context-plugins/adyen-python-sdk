# Account Verification

```python
account_verification_api = client.account_verification
```

## Class Name

`AccountVerificationApi`

## Methods

* [Get-Account Verification-Reports-Code](../../doc/controllers/account-verification.md#get-account-verification-reports-code)
* [Post-Account Verification-Routes](../../doc/controllers/account-verification.md#post-account-verification-routes)


# Get-Account Verification-Reports-Code

Get the account verification report using a unique code from a successful open banking connection. This report provides identity verification and bank account details.

:information_source: **Note** This endpoint does not require authentication.

```python
def get_account_verification_reports_code(self,
                                         code)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `code` | `str` | Template, Required | The unique code you receive after a successful open banking flow that is included as a query parameter in the `redirectUrl` callback.<br><br>**Constraints**: *Minimum Length*: `1` |

## Response Type

**200**: OK - The request has succeeded.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`AccountVerificationReportResponse`](../../doc/models/account-verification-report-response.md).

## Example Usage

```python
code = 'code8'

result = account_verification_api.get_account_verification_reports_code(code)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "id": "nJwJE68h6vlSEnk",
  "country": "US",
  "accounts": [
    {
      "accountId": "XvNzLGMpl3fBevllWEwks3jvBvPy88sbkypkP",
      "accountType": "CURRENT",
      "accountName": "Plaid Gold Standard 0% Interest Checking",
      "accountNumber": "1111222233330000",
      "currency": "USD",
      "identifiers": {
        "ach": {
          "accountNumber": "1111222233330000",
          "routingNumber": "011401533"
        }
      },
      "parties": [
        {
          "identity": {
            "fullLegalName": "Jane Doe",
            "name": "Jane Doe"
          },
          "role": "HOLDER"
        }
      ],
      "bankName": "Wells Fargo"
    },
    {
      "accountId": "XvNzLGMpl3fBevllWEwks3jvBvPy88sbkypkP",
      "accountType": "CURRENT",
      "accountName": "Plaid Gold Standard 0% Interest Checking",
      "accountNumber": "3333222211110000",
      "currency": "USD",
      "identifiers": {
        "ach": {
          "accountNumber": "3333222211110000",
          "routingNumber": "033587521"
        }
      },
      "parties": [
        {
          "identity": {
            "fullLegalName": "Jane Doe",
            "name": "Jane Doe"
          },
          "role": "HOLDER"
        }
      ],
      "bankName": "Bank of America"
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - The request is malformed or is not in the expected format. | [`AccountVerificationReports400ErrorException`](../../doc/models/account-verification-reports-400-error-exception.md) |
| 401 | Unauthorized - The API credential used in the request is invalid or does not have the right permissions. | [`AccountVerificationReports401ErrorException`](../../doc/models/account-verification-reports-401-error-exception.md) |
| 404 | Not Found - The entity was not found. | [`AccountVerificationReports404ErrorException`](../../doc/models/account-verification-reports-404-error-exception.md) |
| 422 | Unprocessable Entity - A request validation error. | [`AccountVerificationReports422ErrorException`](../../doc/models/account-verification-reports-422-error-exception.md) |
| 429 | Too Many Requests - Request rate limit exceeded. | [`AccountVerificationReports429ErrorException`](../../doc/models/account-verification-reports-429-error-exception.md) |
| 500 | Internal Service Error - An unrecoverable error occurred while trying to perform the request. | [`AccountVerificationReports500ErrorException`](../../doc/models/account-verification-reports-500-error-exception.md) |


# Post-Account Verification-Routes

Create a list of routes for verifying bank accounts of third-party individuals. Successful connections generate a unique code used for requesting bank reports and verifying identity.

:information_source: **Note** This endpoint does not require authentication.

```python
def post_account_verification_routes(self,
                                    body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`AccountVerificationRoutesRequest`](../../doc/models/account-verification-routes-request.md) | Body, Required | - |

## Response Type

**200**: OK - The request has succeeded.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`AccountVerificationRoutesResponse`](../../doc/models/account-verification-routes-response.md).

## Example Usage

```python
body = AccountVerificationRoutesRequest(
    country=AccountVerificationCountry2.NL,
    redirect_url='https://merchanturl.example.org/redirect/url',
    locale='en-US',
    state='11a1e60a-18b0-4dda-9258-e0ae29e1e2a3'
)

result = account_verification_api.post_account_verification_routes(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "routes": [
    {
      "provider": {
        "name": "Tink",
        "logoURL": "https://obgateway.adyen.com/obgateway/static/provider/images/tink-logo.svg"
      },
      "link": "https://obgateway.adyen.com/obgateway/provider/outgoing/tink/redirect/13ec4802-c987-4f8c-8909-9a75ff567256"
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - The request is malformed or is not in the expected format. | [`AccountVerificationRoutes400ErrorException`](../../doc/models/account-verification-routes-400-error-exception.md) |
| 401 | Unauthorized - The API credential used in the request is invalid or does not have the right permissions. | [`AccountVerificationRoutes401ErrorException`](../../doc/models/account-verification-routes-401-error-exception.md) |
| 422 | Unprocessable Entity - A request validation error. | [`AccountVerificationRoutes422ErrorException`](../../doc/models/account-verification-routes-422-error-exception.md) |
| 429 | Too Many Requests - Request rate limit exceeded. | [`AccountVerificationRoutes429ErrorException`](../../doc/models/account-verification-routes-429-error-exception.md) |
| 500 | Internal Service Error - An unrecoverable error occurred while trying to perform the request. | [`AccountVerificationRoutes500ErrorException`](../../doc/models/account-verification-routes-500-error-exception.md) |

