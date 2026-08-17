# Grantaccounts

```python
grantaccounts_api = client.grantaccounts
```

## Class Name

`GrantaccountsApi`

## Methods

* [Get-Grant Accounts-Id](../../doc/controllers/grantaccounts.md#get-grant-accounts-id)
* [Get-Grant Accounts-Id 1](../../doc/controllers/grantaccounts.md#get-grant-accounts-id-1)


# Get-Grant Accounts-Id

**This endpoint is deprecated.**

Returns the details of the [grant account](https://docs.adyen.com/platforms/capital#grant-account).

```python
def get_grant_accounts_id(self,
                         id)
```

## Authentication

This endpoint requires [clientKey](../../doc/auth/custom-query-parameter.md) **OR** [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The unique identifier of the grant account. |

## Response Type

**200**: OK - the request has succeeded.

[`CapitalGrantAccount`](../../doc/models/capital-grant-account.md)

## Example Usage

```python
id = 'id0'

result = grant_accounts_api.get_grant_accounts_id(id)
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


# Get-Grant Accounts-Id 1

Returns the details of the specified grant account. This account tracks existing grants in your marketplace or platform.

:information_source: **Note** This endpoint does not require authentication.

```python
def get_grant_accounts_id_1(self,
                           id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The unique identifier of the grant account. |

## Response Type

**200**: OK - The request has succeeded.

[`GrantAccount`](../../doc/models/grant-account.md)

## Example Usage

```python
id = 'id0'

result = grant_accounts_api.get_grant_accounts_id_1(id)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 404 | Not Found - The entity was not found. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |
| 422 | Unprocessable Entity - A request validation error. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |

