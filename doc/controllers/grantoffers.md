# Grantoffers

```python
grantoffers_api = client.grantoffers
```

## Class Name

`GrantoffersApi`

## Methods

* [Get-Grant Offers](../../doc/controllers/grantoffers.md#get-grant-offers)
* [Get-Grant Offers-Grant Offer Id](../../doc/controllers/grantoffers.md#get-grant-offers-grant-offer-id)
* [Get-Grant Offers 1](../../doc/controllers/grantoffers.md#get-grant-offers-1)
* [Get-Grant Offers-Id](../../doc/controllers/grantoffers.md#get-grant-offers-id)


# Get-Grant Offers

**This endpoint is deprecated.**

Returns a list of all [grant offers](https://docs.adyen.com/platforms/capital#grant-offers) available for `accountHolderId` specified as a query parameter.

```python
def get_grant_offers(self,
                    account_holder_id)
```

## Authentication

This endpoint requires [clientKey](../../doc/auth/custom-query-parameter.md) **OR** [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_holder_id` | `str` | Query, Required | The unique identifier of the grant account. |

## Response Type

**200**: OK - the request has succeeded.

[`GrantOffers`](../../doc/models/grant-offers.md)

## Example Usage

```python
account_holder_id = 'accountHolderId8'

result = grant_offers_api.get_grant_offers(account_holder_id)
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


# Get-Grant Offers-Grant Offer Id

**This endpoint is deprecated.**

Returns the details of a single grant offer.

```python
def get_grant_offers_grant_offer_id(self,
                                   grant_offer_id)
```

## Authentication

This endpoint requires [clientKey](../../doc/auth/custom-query-parameter.md) **OR** [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `grant_offer_id` | `str` | Template, Required | The unique identifier of the grant offer. |

## Response Type

**200**: OK - the request has succeeded.

[`GrantOffer`](../../doc/models/grant-offer.md)

## Example Usage

```python
grant_offer_id = 'grantOfferId6'

result = grant_offers_api.get_grant_offers_grant_offer_id(grant_offer_id)
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


# Get-Grant Offers 1

Returns a list of all [static offers](https://docs.adyen.com/capital/get-grant-offers/static-offers) available for `accountHolderId` specified as a query parameter. This also includes static offers created for financing amounts that the user selected from [dynamic offers](https://docs.adyen.com/capital/get-grant-offers/dynamic-offers/).

:information_source: **Note** This endpoint does not require authentication.

```python
def get_grant_offers_1(self,
                      account_holder_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_holder_id` | `str` | Query, Required | The unique identifier of the account holder for which you want to get the available static offers.<br><br>**Constraints**: *Minimum Length*: `1` |

## Response Type

**200**: OK - The request has succeeded.

[`GrantOffers`](../../doc/models/grant-offers.md)

## Example Usage

```python
account_holder_id = 'accountHolderId8'

result = grant_offers_api.get_grant_offers_1(account_holder_id)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 404 | Not Found - The entity was not found. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |
| 422 | Unprocessable Entity - A request validation error. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |


# Get-Grant Offers-Id

Returns the details of the specified static offer.

:information_source: **Note** This endpoint does not require authentication.

```python
def get_grant_offers_id(self,
                       id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The unique identifier of the static offer. |

## Response Type

**200**: OK - The request has succeeded.

[`GrantOffer1`](../../doc/models/grant-offer-1.md)

## Example Usage

```python
id = 'id0'

result = grant_offers_api.get_grant_offers_id(id)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 404 | Not Found - The entity was not found. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |
| 422 | Unprocessable Entity - A request validation error. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |

