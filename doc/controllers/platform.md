# Platform

```python
platform_api = client.platform
```

## Class Name

`PlatformApi`

## Methods

* [Get-Balance Platforms-Id](../../doc/controllers/platform.md#get-balance-platforms-id)
* [Get-Balance Platforms-Id-Account Holders](../../doc/controllers/platform.md#get-balance-platforms-id-account-holders)
* [Get-Balance Platforms-Id-Transaction Rules](../../doc/controllers/platform.md#get-balance-platforms-id-transaction-rules)


# Get-Balance Platforms-Id

Returns a balance platform.

```python
def get_balance_platforms_id(self,
                            id)
```

## Authentication

This endpoint requires [clientKey](../../doc/auth/custom-query-parameter.md) **OR** [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The unique identifier of the balance platform. |

## Response Type

**200**: OK - the request has succeeded.

[`BalancePlatform`](../../doc/models/balance-platform.md)

## Example Usage

```python
id = 'id0'

result = platform_api.get_balance_platforms_id(id)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "id": "YOUR_BALANCE_PLATFORM",
  "status": "Active"
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


# Get-Balance Platforms-Id-Account Holders

Returns a paginated list of all the account holders that belong to the balance platform. To fetch multiple pages, use the query parameters.

For example, to limit the page to 5 account holders and to skip the first 20, use `/balancePlatforms/{id}/accountHolders?limit=5&offset=20`.

```python
def get_balance_platforms_id_account_holders(self,
                                            id,
                                            offset=None,
                                            limit=None)
```

## Authentication

This endpoint requires [clientKey](../../doc/auth/custom-query-parameter.md) **OR** [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The unique identifier of the balance platform. |
| `offset` | `int` | Query, Optional | The number of items that you want to skip. |
| `limit` | `int` | Query, Optional | The number of items returned per page, maximum 100 items. By default, the response returns 10 items per page. |

## Response Type

**200**: OK - the request has succeeded.

[`PaginatedAccountHoldersResponse`](../../doc/models/paginated-account-holders-response.md)

## Example Usage

```python
id = 'id0'

result = platform_api.get_balance_platforms_id_account_holders(id)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "accountHolders": [
    {
      "description": "Test-305",
      "legalEntityId": "LE3227C223222D5D8S5S33M4M",
      "reference": "LegalEntity internal error test",
      "id": "AH32272223222B5GFSNSXFFL9",
      "status": "active"
    },
    {
      "description": "Test-751",
      "legalEntityId": "LE3227C223222D5D8S5TT3SRX",
      "reference": "LegalEntity internal error test",
      "id": "AH32272223222B5GFSNVGFFM7",
      "status": "active"
    },
    {
      "description": "Explorer Holder",
      "legalEntityId": "LE3227C223222D5D8S5TT3SRX",
      "reference": "Account from the Explorer Holder",
      "id": "AH32272223222B5GFWNRFFVR6",
      "status": "active"
    }
  ],
  "hasNext": true,
  "hasPrevious": true
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


# Get-Balance Platforms-Id-Transaction Rules

Returns a list of transaction rules associated with a balance platform.

```python
def get_balance_platforms_id_transaction_rules(self,
                                              id)
```

## Authentication

This endpoint requires [clientKey](../../doc/auth/custom-query-parameter.md) **OR** [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The unique identifier of the balance platform. |

## Response Type

**200**: OK - the request has succeeded.

[`TransactionRulesResponse`](../../doc/models/transaction-rules-response.md)

## Example Usage

```python
id = 'id0'

result = platform_api.get_balance_platforms_id_transaction_rules(id)
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

