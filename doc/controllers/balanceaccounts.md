# Balanceaccounts

```python
balanceaccounts_api = client.balanceaccounts
```

## Class Name

`BalanceaccountsApi`

## Methods

* [Post-Balance Accounts](../../doc/controllers/balanceaccounts.md#post-balance-accounts)
* [Get-Balance Accounts-Id](../../doc/controllers/balanceaccounts.md#get-balance-accounts-id)
* [Patch-Balance Accounts-Id](../../doc/controllers/balanceaccounts.md#patch-balance-accounts-id)
* [Get-Balance Accounts-Id-Payment Instruments](../../doc/controllers/balanceaccounts.md#get-balance-accounts-id-payment-instruments)
* [Get-Balance Accounts-Id-Transaction Rules](../../doc/controllers/balanceaccounts.md#get-balance-accounts-id-transaction-rules)


# Post-Balance Accounts

Creates a balance account that holds the funds of the associated account holder.

```python
def post_balance_accounts(self,
                         body=None)
```

## Authentication

This endpoint requires [clientKey](../../doc/auth/custom-query-parameter.md) **OR** [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`BalanceAccountInfo`](../../doc/models/balance-account-info.md) | Body, Optional | - |

## Response Type

**200**: OK - the request has succeeded.

[`BalanceAccount`](../../doc/models/balance-account.md)

## Example Usage

```python
body = BalanceAccountInfo(
    account_holder_id='AH32272223222C5GXTD343TKP',
    description='S.Hopper - Main balance account'
)

result = balance_accounts_api.post_balance_accounts(
    body=body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "accountHolderId": "AH32272223222C5GXTD343TKP",
  "defaultCurrencyCode": "EUR",
  "description": "S.Hopper - Main balance account",
  "timeZone": "Europe/Amsterdam",
  "balances": [
    {
      "available": 0,
      "balance": 0,
      "currency": "EUR",
      "reserved": 0
    }
  ],
  "id": "BA3227C223222H5J4DCGQ9V9L",
  "status": "active"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - a problem reading or understanding the request. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 401 | Unauthorized - authentication required. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |


# Get-Balance Accounts-Id

Returns a balance account and its balances for the default currency and other currencies with a non-zero balance.

```python
def get_balance_accounts_id(self,
                           id)
```

## Authentication

This endpoint requires [clientKey](../../doc/auth/custom-query-parameter.md) **OR** [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The unique identifier of the balance account. |

## Response Type

**200**: OK - the request has succeeded.

[`BalanceAccount`](../../doc/models/balance-account.md)

## Example Usage

```python
id = 'id0'

result = balance_accounts_api.get_balance_accounts_id(id)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "accountHolderId": "AH32272223222B59K6RTQBFNZ",
  "defaultCurrencyCode": "EUR",
  "timeZone": "Europe/Amsterdam",
  "balances": [
    {
      "available": 0,
      "balance": 0,
      "currency": "EUR",
      "reserved": 0,
      "pending": 0,
      "pendingAvailable": 0
    }
  ],
  "id": "BA3227C223222B5BLP6JQC3FD",
  "status": "active"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - a problem reading or understanding the request. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 401 | Unauthorized - authentication required. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |


# Patch-Balance Accounts-Id

Updates a balance account.

```python
def patch_balance_accounts_id(self,
                             id,
                             body=None)
```

## Authentication

This endpoint requires [clientKey](../../doc/auth/custom-query-parameter.md) **OR** [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The unique identifier of the balance account. |
| `body` | [`BalanceAccountUpdateRequest`](../../doc/models/balance-account-update-request.md) | Body, Optional | - |

## Response Type

**200**: OK - the request has succeeded.

[`BalanceAccount`](../../doc/models/balance-account.md)

## Example Usage

```python
id = 'id0'

body = BalanceAccountUpdateRequest(
    time_zone='Europe/Amsterdam'
)

result = balance_accounts_api.patch_balance_accounts_id(
    id,
    body=body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "accountHolderId": "AH32272223222B5GFSNVGFFM7",
  "defaultCurrencyCode": "EUR",
  "timeZone": "Europe/Amsterdam",
  "balances": [
    {
      "available": 0,
      "balance": 0,
      "currency": "EUR",
      "reserved": 0
    }
  ],
  "id": "BA32272223222B59K6ZXHBFN6",
  "status": "active"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - a problem reading or understanding the request. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 401 | Unauthorized - authentication required. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |


# Get-Balance Accounts-Id-Payment Instruments

Returns a paginated list of the payment instruments associated with a balance account.

To fetch multiple pages, use the query parameters.For example, to limit the page to 3 payment instruments which are in active status and to skip the first 6, use `/balanceAccounts/{id}/paymentInstruments?limit=3&offset=6&status=active`.

```python
def get_balance_accounts_id_payment_instruments(self,
                                               id,
                                               offset=None,
                                               limit=None,
                                               status=None)
```

## Authentication

This endpoint requires [clientKey](../../doc/auth/custom-query-parameter.md) **OR** [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The unique identifier of the balance account. |
| `offset` | `int` | Query, Optional | The number of items that you want to skip. |
| `limit` | `int` | Query, Optional | The number of items returned per page, maximum 100 items. By default, the response returns 10 items per page. |
| `status` | `str` | Query, Optional | The status of the payment instruments that you want to get. By default, the response includes payment instruments with any status. |

## Response Type

**200**: OK - the request has succeeded.

[`PaginatedPaymentInstrumentsResponse`](../../doc/models/paginated-payment-instruments-response.md)

## Example Usage

```python
id = 'id0'

result = balance_accounts_api.get_balance_accounts_id_payment_instruments(id)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "hasNext": true,
  "hasPrevious": false,
  "paymentInstruments": [
    {
      "balanceAccountId": "BA32272223222B59CZ3T52DKZ",
      "issuingCountryCode": "GB",
      "status": "active",
      "type": "card",
      "card": {
        "brand": "mc",
        "brandVariant": "mc",
        "cardholderName": "name",
        "formFactor": "virtual",
        "bin": "555544",
        "expiration": {
          "month": "12",
          "year": "2022"
        },
        "lastFour": "2357",
        "number": "************2357"
      },
      "id": "PI32272223222B59M5TM658DT"
    },
    {
      "balanceAccountId": "BA32272223222B59CZ3T52DKZ",
      "issuingCountryCode": "GB",
      "status": "active",
      "type": "card",
      "card": {
        "brand": "mc",
        "brandVariant": "mc",
        "cardholderName": "name",
        "formFactor": "virtual",
        "bin": "555544",
        "expiration": {
          "month": "01",
          "year": "2023"
        },
        "lastFour": "8331",
        "number": "************8331"
      },
      "id": "PI32272223222B59PXDGQDLSF"
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - a problem reading or understanding the request. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 401 | Unauthorized - authentication required. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |


# Get-Balance Accounts-Id-Transaction Rules

Returns a list of transaction rules associated with a balance account.

```python
def get_balance_accounts_id_transaction_rules(self,
                                             id)
```

## Authentication

This endpoint requires [clientKey](../../doc/auth/custom-query-parameter.md) **OR** [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The unique identifier of the balance account. |

## Response Type

**200**: OK - the request has succeeded.

[`TransactionRulesResponse`](../../doc/models/transaction-rules-response.md)

## Example Usage

```python
id = 'id0'

result = balance_accounts_api.get_balance_accounts_id_transaction_rules(id)
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

