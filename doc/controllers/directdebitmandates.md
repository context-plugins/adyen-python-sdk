# Directdebitmandates

```python
directdebitmandates_api = client.directdebitmandates
```

## Class Name

`DirectdebitmandatesApi`

## Methods

* [Get-Mandates](../../doc/controllers/directdebitmandates.md#get-mandates)
* [Get-Mandates-Mandate Id](../../doc/controllers/directdebitmandates.md#get-mandates-mandate-id)
* [Patch-Mandates-Mandate Id](../../doc/controllers/directdebitmandates.md#patch-mandates-mandate-id)
* [Post-Mandates-Mandate Id-Cancel](../../doc/controllers/directdebitmandates.md#post-mandates-mandate-id-cancel)


# Get-Mandates

Returns a list of all [direct debit mandates](https://docs.adyen.com/business-accounts/accept-direct-debits-uk) created for a business account.

:information_source: **Note** This endpoint does not require authentication.

```python
def get_mandates(self,
                balance_account_id=None,
                payment_instrument_id=None,
                cursor=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `balance_account_id` | `str` | Query, Optional | The unique identifier of the balance account linked to the payment instrument. |
| `payment_instrument_id` | `str` | Query, Optional | The unique identifier of the payment instrument linked to the mandate. |
| `cursor` | `str` | Query, Optional | The pagination cursor returned in a previous GET `/mandates` request. |

## Response Type

**200**: OK - The request has succeeded

[`ListMandatesResponse`](../../doc/models/list-mandates-response.md)

## Example Usage

```python
result = direct_debit_mandates_api.get_mandates()
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized - authentication required. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |


# Get-Mandates-Mandate Id

Returns the details of the specified [direct debit mandate](https://docs.adyen.com/business-accounts/accept-direct-debits-uk).

:information_source: **Note** This endpoint does not require authentication.

```python
def get_mandates_mandate_id(self,
                           mandate_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mandate_id` | `str` | Template, Required | The unique identifier of the mandate. |

## Response Type

**200**: OK - The request has succeeded

[`Mandate1`](../../doc/models/mandate-1.md)

## Example Usage

```python
mandate_id = 'mandateId8'

result = direct_debit_mandates_api.get_mandates_mandate_id(mandate_id)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized - authentication required. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |
| 404 | The mandate was not found. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |


# Patch-Mandates-Mandate Id

Amend the specified [direct debit mandate](https://docs.adyen.com/business-accounts/accept-direct-debits-uk).

:information_source: **Note** This endpoint does not require authentication.

```python
def patch_mandates_mandate_id(self,
                             mandate_id,
                             body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mandate_id` | `str` | Template, Required | The unique identifier of the mandate. |
| `body` | [`MandateUpdate`](../../doc/models/mandate-update.md) | Body, Required | - |

## Response Type

**202**: Accepted - The request has been accepted

`void`

## Example Usage

```python
mandate_id = 'mandateId8'

body = MandateUpdate()

direct_debit_mandates_api.patch_mandates_mandate_id(
    mandate_id,
    body
)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized - authentication required. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |
| 404 | The mandate was not found | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |


# Post-Mandates-Mandate Id-Cancel

Cancel a specified [direct debit mandate](https://docs.adyen.com/business-accounts/accept-direct-debits-uk).

:information_source: **Note** This endpoint does not require authentication.

```python
def post_mandates_mandate_id_cancel(self,
                                   mandate_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mandate_id` | `str` | Template, Required | The unique identifier of the mandate. |

## Response Type

**202**: Accepted - The request has been accepted

`void`

## Example Usage

```python
mandate_id = 'mandateId8'

direct_debit_mandates_api.post_mandates_mandate_id_cancel(mandate_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized - authentication required. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |
| 404 | The mandate was not found. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |

