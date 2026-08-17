# Capital

```python
capital_api = client.capital
```

## Class Name

`CapitalApi`

## Methods

* [Get-Grants](../../doc/controllers/capital.md#get-grants)
* [Post-Grants](../../doc/controllers/capital.md#post-grants)
* [Get-Grants-Id](../../doc/controllers/capital.md#get-grants-id)


# Get-Grants

**This endpoint is deprecated.**

Returns a list of grants with status and outstanding balances.

```python
def get_grants(self,
              counterparty_account_holder_id=None)
```

## Authentication

This endpoint requires [clientKey](../../doc/auth/custom-query-parameter.md) **OR** [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `counterparty_account_holder_id` | `str` | Query, Optional | The counterparty account holder id. |

## Response Type

**200**: OK - the request has succeeded.

[`CapitalGrants`](../../doc/models/capital-grants.md)

## Example Usage

```python
result = capital_api.get_grants()
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - a problem reading or understanding the request. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 401 | Unauthorized - authentication required. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 404 | Not Found - the payment was not found | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |


# Post-Grants

**This endpoint is deprecated.**

Requests the payout of the selected grant offer.

```python
def post_grants(self,
               idempotency_key=None,
               body=None)
```

## Authentication

This endpoint requires [clientKey](../../doc/auth/custom-query-parameter.md) **OR** [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `idempotency_key` | `str` | Header, Optional | A unique identifier for the message with a maximum of 64 characters (we recommend a UUID). |
| `body` | [`CapitalGrantInfo`](../../doc/models/capital-grant-info.md) | Body, Optional | - |

## Response Type

**200**: OK - the request has succeeded.

[`CapitalGrant`](../../doc/models/capital-grant.md)

## Example Usage

```python
body = CapitalGrantInfo(
    grant_account_id='CG00000000000000000000001',
    grant_offer_id='0000000000000001',
    counterparty=GrantInfoCounterparty2(
        balance_account_id='BA00000000000000000000001'
    )
)

result = capital_api.post_grants(
    body=body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "id": "GR00000000000000000000001",
  "grantAccountId": "CG00000000000000000000001",
  "grantOfferId": "0000000000000001",
  "counterparty": {
    "accountHolderId": "AH00000000000000000000001",
    "balanceAccountId": "BA00000000000000000000001"
  },
  "amount": {
    "currency": "EUR",
    "value": 1000000
  },
  "fee": {
    "amount": {
      "value": 120000,
      "currency": "EUR"
    }
  },
  "balances": {
    "currency": "EUR",
    "fee": 120000,
    "principal": 1000000,
    "total": 1120000
  },
  "repayment": {
    "basisPoints": 1400
  },
  "status": "Pending"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - a problem reading or understanding the request. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 401 | Unauthorized - authentication required. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 404 | Not Found - the payment was not found | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |


# Get-Grants-Id

**This endpoint is deprecated.**

Returns the details of a capital account specified in the path.

```python
def get_grants_id(self,
                 id)
```

## Authentication

This endpoint requires [clientKey](../../doc/auth/custom-query-parameter.md) **OR** [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The unique identifier of the grant. |

## Response Type

**200**: OK - the request has succeeded.

[`CapitalGrant`](../../doc/models/capital-grant.md)

## Example Usage

```python
id = 'id0'

result = capital_api.get_grants_id(id)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - a problem reading or understanding the request. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 401 | Unauthorized - authentication required. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 404 | Not Found - the payment was not found | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |

