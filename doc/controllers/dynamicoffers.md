# Dynamicoffers

```python
dynamicoffers_api = client.dynamicoffers
```

## Class Name

`DynamicoffersApi`

## Methods

* [Get-Dynamic Offers](../../doc/controllers/dynamicoffers.md#get-dynamic-offers)
* [Post-Dynamic Offers-Id-Calculate](../../doc/controllers/dynamicoffers.md#post-dynamic-offers-id-calculate)
* [Post-Dynamic Offers-Id-Grant Offer](../../doc/controllers/dynamicoffers.md#post-dynamic-offers-id-grant-offer)


# Get-Dynamic Offers

Returns a list of all [dynamic offers](https://docs.adyen.com/capital/get-grant-offers/dynamic-offers/) available for `accountHolderId` specified as a query parameter.

:information_source: **Note** This endpoint does not require authentication.

```python
def get_dynamic_offers(self,
                      account_holder_id,
                      financing_type=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_holder_id` | `str` | Query, Required | The unique identifier of the account holder that the dynamic offer is for.<br><br>**Constraints**: *Minimum Length*: `1` |
| `financing_type` | [`FinancingTypeEnum`](../../doc/models/financing-type-enum.md) | Query, Optional | The type of financing that the offer is for. If the value is not specified, returns all available types.<br><br>Possible values: **businessFinancing** |

## Response Type

**200**: OK - The request has succeeded.

[`GetDynamicOffersResponse`](../../doc/models/get-dynamic-offers-response.md)

## Example Usage

```python
account_holder_id = 'accountHolderId8'

result = dynamic_offers_api.get_dynamic_offers(account_holder_id)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 422 | Unprocessable Entity - A request validation error. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |


# Post-Dynamic Offers-Id-Calculate

Calculates a preliminary offer for the financing amount that the user selected from a [dynamic offer](https://docs.adyen.com/capital/get-grant-offers/dynamic-offers/). The preliminary offer is for informational purposes only and cannot be used to initiate a grant.

Requests to this endpoint are subject to rate limits:

- Live environments: 120 requests per minute.

- Test environments: 120 requests per minute.

:information_source: **Note** This endpoint does not require authentication.

```python
def post_dynamic_offers_id_calculate(self,
                                    id,
                                    body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The unique identifier of the dynamic offer from which the user selected the financing amount.<br><br>**Constraints**: *Minimum Length*: `1` |
| `body` | [`CalculateGrantOfferRequest`](../../doc/models/calculate-grant-offer-request.md) | Body, Optional | - |

## Response Type

**200**: OK - The request has succeeded.

[`CalculatedGrantOffer`](../../doc/models/calculated-grant-offer.md)

## Example Usage

```python
id = 'id0'

result = dynamic_offers_api.post_dynamic_offers_id_calculate(id)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 422 | Unprocessable Entity - A request validation error. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |


# Post-Dynamic Offers-Id-Grant Offer

Creates a static offer for the financing amount that the user selected from the [dynamic offer](https://docs.adyen.com/capital/get-grant-offers/dynamic-offers/).

Requests to this endpoint are subject to rate limits:

- Live environments: 30 requests per minute.

- Test environments: 30 requests per minute.

:information_source: **Note** This endpoint does not require authentication.

```python
def post_dynamic_offers_id_grant_offer(self,
                                      id,
                                      body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The unique identifier of the dynamic offer from which the user selected the financing amount.<br><br>**Constraints**: *Minimum Length*: `1` |
| `body` | [`CreateGrantOfferRequest`](../../doc/models/create-grant-offer-request.md) | Body, Optional | - |

## Response Type

**200**: OK - The request has succeeded.

[`GrantOffer1`](../../doc/models/grant-offer-1.md)

## Example Usage

```python
id = 'id0'

result = dynamic_offers_api.post_dynamic_offers_id_grant_offer(id)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 422 | Unprocessable Entity - A request validation error. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |

