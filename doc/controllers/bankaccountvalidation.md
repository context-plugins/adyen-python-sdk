# Bankaccountvalidation

```python
bankaccountvalidation_api = client.bankaccountvalidation
```

## Class Name

`BankaccountvalidationApi`


# Post-Validate Bank Account Identification

Validates bank account identification details. You can use this endpoint to validate bank account details before you [make a transfer](https://docs.adyen.com/api-explorer/transfers/latest/post/transfers) or [create a transfer instrument](https://docs.adyen.com/api-explorer/legalentity/latest/post/transferInstruments).

```python
def post_validate_bank_account_identification(self,
                                             body=None)
```

## Authentication

This endpoint requires [clientKey](../../doc/auth/custom-query-parameter.md) **OR** [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`BankAccountIdentificationValidationRequest`](../../doc/models/bank-account-identification-validation-request.md) | Body, Optional | - |

## Response Type

**200**: No Content - look at the actual response code for the status of the request.

`void`

## Example Usage

```python
body = BankAccountIdentificationValidationRequest(
    account_identification=IbanAccountIdentification(
        iban='1001001234'
    )
)

bank_account_validation_api.post_validate_bank_account_identification(
    body=body
)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized - authentication required. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |

