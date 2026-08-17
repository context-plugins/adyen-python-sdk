# Transactions

```python
transactions_api = client.transactions
```

## Class Name

`TransactionsApi`

## Methods

* [Get-Transactions](../../doc/controllers/transactions.md#get-transactions)
* [Get-Transactions-Id](../../doc/controllers/transactions.md#get-transactions-id)


# Get-Transactions

> Versions 1 and 2 of the Transfers API are deprecated. If you are just starting your implementation, use the latest version.

Returns all the transactions related to a balance account, account holder, or balance platform.

When making this request, you must include at least one of the following:

- `balanceAccountId`
- `accountHolderId`
- `balancePlatform`.

This endpoint supports cursor-based pagination. The response returns the first page of results, and returns links to the next and previous pages when applicable. You can use the links to page through the results.

```python
def get_transactions(self,
                    created_since,
                    created_until,
                    balance_platform=None,
                    payment_instrument_id=None,
                    account_holder_id=None,
                    balance_account_id=None,
                    cursor=None,
                    sort_order=None,
                    limit=None)
```

## Authentication

This endpoint requires [clientKey](../../doc/auth/custom-query-parameter.md) **OR** [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `created_since` | `datetime` | Query, Required | Only include transactions that have been created on or after this point in time. The value must be in ISO 8601 format. For example, **2021-05-30T15:07:40Z**. |
| `created_until` | `datetime` | Query, Required | Only include transactions that have been created on or before this point in time. The value must be in ISO 8601 format. For example, **2021-05-30T15:07:40Z**. |
| `balance_platform` | `str` | Query, Optional | The unique identifier of the [balance platform](https://docs.adyen.com/api-explorer/#/balanceplatform/latest/get/balancePlatforms/{id}__queryParam_id).<br><br>Required if you don't provide a `balanceAccountId` or `accountHolderId`. |
| `payment_instrument_id` | `str` | Query, Optional | The unique identifier of the [payment instrument](https://docs.adyen.com/api-explorer/balanceplatform/latest/get/paymentInstruments/_id_).<br><br>To use this parameter, you must also provide a `balanceAccountId`, `accountHolderId`, or `balancePlatform`.<br><br>The `paymentInstrumentId` must be related to the `balanceAccountId` or `accountHolderId` that you provide. |
| `account_holder_id` | `str` | Query, Optional | The unique identifier of the [account holder](https://docs.adyen.com/api-explorer/#/balanceplatform/latest/get/accountHolders/{id}__queryParam_id).<br><br>Required if you don't provide a `balanceAccountId` or `balancePlatform`.<br><br>If you provide a `balanceAccountId`, the `accountHolderId` must be related to the `balanceAccountId`. |
| `balance_account_id` | `str` | Query, Optional | The unique identifier of the [balance account](https://docs.adyen.com/api-explorer/#/balanceplatform/latest/get/balanceAccounts/{id}__queryParam_id).<br><br>Required if you don't provide an `accountHolderId` or `balancePlatform`.<br><br>If you provide an `accountHolderId`, the `balanceAccountId` must be related to the `accountHolderId`. |
| `cursor` | `str` | Query, Optional | The `cursor` returned in the links of the previous response. |
| `sort_order` | [`SortOrderEnum`](../../doc/models/sort-order-enum.md) | Query, Optional | Determines the sort order of the returned transactions. The sort order is based on the creation date of the transaction.<br><br>Possible values:<br><br>- **asc**: Ascending order, from oldest to most recent.<br><br>- **desc**: Descending order, from most recent to oldest.<br><br>Default value: **asc**. |
| `limit` | `int` | Query, Optional | The number of items returned per page, maximum of 100 items. By default, the response returns 10 items per page. |

## Response Type

**200**: OK - the request has succeeded.

[`TransactionSearchResponse`](../../doc/models/transaction-search-response.md)

## Example Usage

```python
created_since = dateutil.parser.parse('2016-03-13T12:52:32.123Z')

created_until = dateutil.parser.parse('2016-03-13T12:52:32.123Z')

result = transactions_api.get_transactions(
    created_since,
    created_until
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "data": [
    {
      "balancePlatform": "YOUR_BALANCE_PLATFORM",
      "creationDate": "2023-08-10T14:51:20+02:00",
      "id": "EVJN42272224222B5JB8BRC84N686ZEUR",
      "accountHolder": {
        "description": "Your description for the account holder",
        "id": "AH00000000000000000000001"
      },
      "amount": {
        "currency": "USD",
        "value": -1000
      },
      "balanceAccount": {
        "description": "Your description for the account holder",
        "id": "BA00000000000000000000001"
      },
      "bookingDate": "2023-08-10T14:51:33+02:00",
      "status": "booked",
      "transfer": {
        "id": "3JNC3O5ZVFLLGV4B",
        "reference": "Your internal reference for the transfer"
      },
      "valueDate": "2023-08-10T14:51:20+02:00"
    },
    {
      "balancePlatform": "YOUR_BALANCE_PLATFORM",
      "creationDate": "2023-08-10T15:34:31+02:00",
      "id": "EVJN4227C224222B5JB8G3Q89N2NB6EUR",
      "accountHolder": {
        "description": "Your description for the account holder",
        "id": "AH00000000000000000000001"
      },
      "amount": {
        "currency": "USD",
        "value": 123
      },
      "balanceAccount": {
        "description": "Your description for the account holder",
        "id": "BA00000000000000000000001"
      },
      "bookingDate": "2023-08-10T15:34:40+02:00",
      "status": "booked",
      "transfer": {
        "id": "48POO45ZVG11166J",
        "reference": "Your internal reference for the transfer"
      },
      "valueDate": "2023-08-10T15:34:31+02:00"
    },
    {
      "balancePlatform": "YOUR_BALANCE_PLATFORM",
      "creationDate": "2023-08-11T13:45:46+02:00",
      "id": "EVJN4227C224222B5JBD3XHF8P3L8GUSD",
      "accountHolder": {
        "description": "Your description for the account holder",
        "id": "AH00000000000000000000001"
      },
      "amount": {
        "currency": "USD",
        "value": -10000
      },
      "balanceAccount": {
        "description": "Your description for the account holder",
        "id": "BA00000000000000000000001"
      },
      "bookingDate": "2023-08-11T13:45:57+02:00",
      "status": "booked",
      "transfer": {
        "id": "48RTTW5ZVT8KU9DV",
        "reference": "my-reference"
      },
      "valueDate": "2023-08-11T13:45:46+02:00"
    },
    {
      "balancePlatform": "YOUR_BALANCE_PLATFORM",
      "creationDate": "2023-08-11T13:45:51+02:00",
      "id": "EVJN42272224222B5JBD3XJGHF4J26USD",
      "accountHolder": {
        "description": "Your description for the account holder",
        "id": "AH00000000000000000000001"
      },
      "amount": {
        "currency": "USD",
        "value": 1000
      },
      "balanceAccount": {
        "description": "Your description for the account holder",
        "id": "BA00000000000000000000001"
      },
      "bookingDate": "2023-08-11T13:45:58+02:00",
      "status": "booked",
      "transfer": {
        "id": "48TYZO5ZVT8M1K47",
        "reference": "my-reference"
      },
      "valueDate": "2023-08-11T13:45:51+02:00"
    }
  ],
  "_links": {
    "next": {
      "href": "https://balanceplatform-api-test.adyen.com/btl/v4/transactions?balancePlatform=TestBalancePlatform&createdUntil=2023-08-20T13%3A07%3A40Z&createdSince=2023-08-10T10%3A50%3A40Z&cursor=S2B-c0p1N0tdN0l6RGhYK1YpM0lgOTUyMDlLXElyKE9LMCtyaFEuMj1NMHgidCsrJi1ZNnhqXCtqVi5JPGpRK1F2fCFqWzU33JTojSVNJc1J1VXhncS10QDd6JX9FQFl5Zn0uNyUvSXJNQTo"
    }
  }
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized - authentication required. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |


# Get-Transactions-Id

> Versions 1 and 2 of the Transfers API are deprecated. If you are just starting your implementation, use the latest version.

Returns a transaction.

```python
def get_transactions_id(self,
                       id)
```

## Authentication

This endpoint requires [clientKey](../../doc/auth/custom-query-parameter.md) **OR** [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The unique identifier of the transaction. |

## Response Type

**200**: OK - the request has succeeded.

[`Transaction`](../../doc/models/transaction.md)

## Example Usage

```python
id = 'id0'

result = transactions_api.get_transactions_id(id)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "id": "EVJN4227C224222B5JBDHPTD672M52EUR",
  "amount": {
    "value": -10000,
    "currency": "EUR"
  },
  "status": "booked",
  "transfer": {
    "id": "48TYZO5ZVURJ2FCW",
    "reference": "Your internal reference for the transfer"
  },
  "valueDate": "2023-08-11T16:19:35+02:00",
  "bookingDate": "2023-08-11T16:19:39+02:00",
  "creationDate": "2023-08-11T16:19:35+02:00",
  "accountHolder": {
    "id": "AH00000000000000000000001",
    "description": "Your description of the account holder"
  },
  "balanceAccount": {
    "id": "BA00000000000000000000001",
    "description": "Your description of the balance account"
  },
  "balancePlatform": "YOUR_BALANCE_PLATFORM"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized - authentication required. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |

