# Transferroutes

```python
transferroutes_api = client.transferroutes
```

## Class Name

`TransferroutesApi`


# Post-Transfer Routes-Calculate

Returns available transfer routes based on a combination of transfer `country`, `currency`, `counterparty`, and `priorities`. Use this endpoint to find optimal transfer priorities and associated requirements before you [make a transfer](https://docs.adyen.com/api-explorer/transfers/latest/post/transfers).

```python
def post_transfer_routes_calculate(self,
                                  body=None)
```

## Authentication

This endpoint requires [clientKey](../../doc/auth/custom-query-parameter.md) **OR** [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`TransferRouteRequest`](../../doc/models/transfer-route-request.md) | Body, Optional | - |

## Response Type

**200**: OK - the request has succeeded.

[`TransferRouteResponse`](../../doc/models/transfer-route-response.md)

## Example Usage

```python
body = TransferRouteRequest(
    balance_platform='YOUR_BALANCE_PLATFORM',
    currency='USD',
    counterparty=Counterparty1(
        bank_account=BankAccount11(
            account_identification=IbanAccountIdentification(
                iban='NL91ABNA0417164300'
            )
        )
    )
)

result = transfer_routes_api.post_transfer_routes_calculate(
    body=body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "transferRoutes": [
    {
      "country": "NL",
      "currency": "USD",
      "priority": "crossBorder",
      "requirements": [
        {
          "description": "Amount of transfer must be at least 100, and no greater than 99999999999",
          "max": 99999999999,
          "min": 100,
          "type": "amountMinMaxRequirement"
        },
        {
          "description": "Country, street and city is required.",
          "requiredAddressFields": [
            "line1",
            "city",
            "country"
          ],
          "type": "addressRequirement"
        },
        {
          "description": "Bank account identification type must be iban or numberAndBic",
          "bankAccountIdentificationTypes": [
            "iban",
            "numberAndBic"
          ],
          "type": "bankAccountIdentificationTypeRequirement"
        },
        {
          "issuingCountryCode": "NL",
          "paymentInstrumentType": "BankAccount",
          "type": "paymentInstrumentRequirement"
        }
      ]
    },
    {
      "country": "NL",
      "currency": "USD",
      "priority": "wire",
      "requirements": [
        {
          "description": "Amount of transfer must be at least 100, and no greater than 99999999999",
          "max": 99999999999,
          "min": 100,
          "type": "amountMinMaxRequirement"
        },
        {
          "description": "Country, street and city is required.",
          "requiredAddressFields": [
            "line1",
            "city",
            "country"
          ],
          "type": "addressRequirement"
        },
        {
          "description": "Bank account identification type must be iban or numberAndBic",
          "bankAccountIdentificationTypes": [
            "iban",
            "numberAndBic"
          ],
          "type": "bankAccountIdentificationTypeRequirement"
        },
        {
          "issuingCountryCode": "NL",
          "paymentInstrumentType": "BankAccount",
          "type": "paymentInstrumentRequirement"
        }
      ]
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized - authentication required. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |

