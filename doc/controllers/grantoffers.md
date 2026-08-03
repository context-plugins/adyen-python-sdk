# Grantoffers

```python
grantoffers_api = client.grantoffers
```

## Class Name

`GrantoffersApi`

## Methods

* [Get-Grant Offers](../../doc/controllers/grantoffers.md#get-grant-offers)
* [Get-Grant Offers-Grant Offer Id](../../doc/controllers/grantoffers.md#get-grant-offers-grant-offer-id)
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

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`GrantOffers`](../../doc/models/grant-offers.md).

## Example Usage

```python
account_holder_id = 'accountHolderId8'

result = grant_offers_api.get_grant_offers(account_holder_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
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

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`GrantOffer`](../../doc/models/grant-offer.md).

## Example Usage

```python
grant_offer_id = 'grantOfferId6'

result = grant_offers_api.get_grant_offers_grant_offer_id(grant_offer_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - a problem reading or understanding the request. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 401 | Unauthorized - authentication required. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |


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

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`GrantOffer1`](../../doc/models/grant-offer-1.md).

## Example Usage

```python
id = 'id0'

result = grant_offers_api.get_grant_offers_id(id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 404 | Not Found - The entity was not found. | [`GrantOffers404ErrorException`](../../doc/models/grant-offers-404-error-exception.md) |
| 422 | Unprocessable Entity - A request validation error. | [`GrantOffers422Error3Exception`](../../doc/models/grant-offers-422-error-3-exception.md) |

